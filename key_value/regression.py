#!/usr/bin/env python3
import os
import sys

from testflows.core import *

append_path(sys.path, "..")

from helpers.cluster import Cluster
from key_value.requirements.requirements import *
from helpers.argparser import argparser as argparser
from helpers.common import check_clickhouse_version

xfails = {}

xflags = {}

ffails = {}


@TestModule
@ArgumentParser(argparser)
@XFails(xfails)
@XFlags(xflags)
@FFails(ffails)
@Name("key value")
@Specifications(SRS033_ClickHouse_Key_Value_Function)
@Requirements(RQ_SRS_033_ClickHouse_ParseKeyValue_Function("1.0"))
def regression(
    self,
    local,
    clickhouse_binary_path,
    clickhouse_version,
    stress=None,
    parallel=None,
):
    """Key Value regression."""
    nodes = {"clickhouse": ("clickhouse1", "clickhouse2", "clickhouse3")}

    self.context.clickhouse_version = clickhouse_version

    with Cluster(
        local,
        clickhouse_binary_path,
        nodes=nodes,
        docker_compose_project_dir=os.path.join(
            current_dir(), os.path.basename(current_dir()) + "_env"
        ),
    ) as cluster:
        self.context.cluster = cluster
        self.context.stress = stress

        if parallel is not None:
            self.context.parallel = parallel

        Feature(run=load("key_value.tests.constant", "feature"))
        Feature(run=load("key_value.tests.column", "feature"))


if main():
    regression()
