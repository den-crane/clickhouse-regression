from testflows.core import *

from aggregate_functions.requirements import (
    RQ_SRS_031_ClickHouse_AggregateFunctions_Specific_GroupArrayMovingSum,
)

from aggregate_functions.tests.groupArrayMovingAvg import feature as checks


@TestFeature
@Name("groupArrayMovingSum")
@Requirements(RQ_SRS_031_ClickHouse_AggregateFunctions_Specific_GroupArrayMovingSum("1.0"))
def feature(self, func="groupArrayMovingSum({params})", table=None):
    """Check groupArrayMovingSum aggregate function by using the same tests as for groupArrayMovingAvg."""
    self.context.snapshot_id = name.basename(current().name)

    if table is None:
        table = self.context.table

    checks(func=func, table=table)