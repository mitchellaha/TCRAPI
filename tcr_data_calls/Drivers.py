from tcr_interactions.get_grid import getGridDataFields, getGridQuickSearchFields
from tcr_interactions.get_user_settings import getGridSortSettings
from tcr_interactions.post_models import ConditionsModel, FilterModel, FilterSearchConditionsModel, FilterSearchModel

class driversClass:
    def __init__(self):
        self.gridID = 34
        self.gridName = "DRIVERS"
        self.Attributes = getGridDataFields(self.gridID)
        self.gridCustomSort = getGridSortSettings(self.gridID)
        self.filterConditions = FilterModel(
            Conditions=[
                ConditionsModel(
                    Attribute="Status",
                    Values=["A"],
                    Operator=12
                ),
            ]
        )

    def search(self, SearchQuery):
        AttributeList = getGridQuickSearchFields(self.gridID)
        Conditions = []
        for Attribute in AttributeList:
            Conditions.append(
                ConditionsModel(
                    Attribute=Attribute,
                    Values=[
                        SearchQuery
                    ],
                    Operator=10
                )
            )
        respond = FilterSearchModel(
            Conditions=[self.filterConditions.Conditions[0]],
            Filter=FilterSearchConditionsModel(
                Conditions=Conditions,
                GroupOperator=2
            )
        )
        return respond