# References


# TCRAPI.*auth*(email, password)  -  Class Object

- **email**: Your TCR email address : str
    - Default is None
    - If None, the email will be retrieved from the environment variable "email"
- **password**: Your TCR password : str
    - Default is None
    - If None, the password will be retrieved from the environment variable "password"


## Instance Methods

#### TCRAPI.*auth()*.get_cookies()

Gets Net Cookies from TCR with BeautifulSoup & Requests

- **Returns:**
    - cookies[0] : dict
    - expiration[1] : dict


#### TCRAPI.*auth()*.set_header()

Gets new request headers for the TCRAPI.auth object.

- Sets the following for the instance:
    - auth.header : dict
        - contains the full headers to be used in tcr requests
    - auth.cookies : dict
        - contains the cookies used in the headers
    - auth.expire : dict
        - contains the expiration date of the cookies in epoch time

- **Returns:**
    - auth.header : dict


--------------------------------


# TCRAPI.*api*(email, password)  -  Class Object

- **email**: TCR login Email
- **password**: TCR login Password

## Instance Methods

#### TCRAPI.*api()*.getGrid(gridName)

Returns Information for the specified Grid.  
Uses the "GetGrid" API call which Only Uses the Grid Name.  
Will Convert the Grid Name to the Grid ID using the "GetGridByID" API call.

- **gridName**: The name or ID of the grid : str | int 

- **Returns:**
    - all grid information : dict


#### TCRAPI.*api()*.getGridByID(gridID)

Returns Information for the specified Grid.
Uses the "GetGridByID" API call which Uses the Grid ID.
Will Convert the Grid ID to the Grid Name using the "GetGrid" API call.

- **gridID**: The name or ID of the grid : int | str

- **Returns:**
    - all grid information : dict


#### TCRAPI.*api()*.getGridByName(gridName)

Converts The Grid Name To Grid ID and Vice Versa.

- **grid**: The name or ID of the grid : str | int

- **Returns:**
    - gridID : int / gridName : str


#### TCRAPI.*api()*.getGridInfo(grid)

Gets a few pieces of relevant information for the specified Grid.

- **grid**: The type of grid to get : str | int

- **Returns:**
    - gridInfo : dict
        - GridTitle : str
        - GridName : str
        - GridID : int
        - PrimaryKeyField : str
        - EditURL : str
        - FilterFields : None | str
        - Columns : list


#### TCRAPI.*api()*.getGridDataFields(grid)

Gets The Required Field Attributes for the specified Grid.
**ONLY RETURNS THE FIELD ATTRIBUTES**.

- **grid**: The type of grid to get : str | int

- **Returns:**
    - dataFields : list


#### TCRAPI.*api()*.getGridDataFieldsInfo(grid, filters, page, pageSize)

**TODO**


#### TCRAPI.*api()*.getGridQuickSearchFields(grid)

Gets The QuickSearch Fields for the specified Grid.  
Used for .getGridDate(*QuickSearch=*)

-- **grid**: The type of grid to get : str | int

- **Returns:**
    - quickSearchFields : list


#### TCRAPI.*api()*.getUserSettings(settingName)

Gets The User Settings from TCR

- **settingName**: The name of the setting to get : str

- **Returns:**
    - userSettings : dict


#### TCRAPI.*api()*.getGridSettings(grid)

Gets The Grid Settings from TCR.  
Formats the Setting Name as "Yagna.Grid.*grid*"

- **grid**: The type of grid to get : str | int

- **Returns:**
    - gridSettings : dict


#### TCRAPI.*api()*.getGridSortSettings(grid)

Gets User Sort Settings from TCR if they exist.  
If Not the gets the default sort settings from .getGrid()  
Used for .getGridData()

- **grid**: The type of grid to get : str | int

- **Returns:**
    - SortModel : BaseClass with the following attributes:
        - Attrubute = Attribute to Sort By : str
        - Order = Sort Direction : int


#### TCRAPI.*api()*.getSideMenus()

Gets the Side Menus from TCR.

- **Returns:**
    - sideMenus : list of dict


#### TCRAPI.*api()*.getColumnsForAdvSearch(grid)

Gets the Columns for Advanced Search from TCR.  
Uses GetGridColumnsForAdvSearch API Call.

- **grid**: The type of grid to get : str | int

- **Returns:**
    - columns : list of dict


#### TCRAPI.*api()*.getGridData(gGrid, FilterConditions, StartIndex, RecordCount, QuickSearch, IncludeCount)

Gets the Data for the specified Grid.  
Uses the "GetGridData" API call.

- **Grid**: The Grid To Retrieve : str | int
    - **TODO**
- **FilterConditions**: The Filter Conditions to use : list
    - **TODO**
- **StartIndex**: The Starting Row For The API Call : int
    - Optional - Default is 1
- **RecordCount**: The Number of Rows to Return : int
    - Optional - Default is 250
- **QuickSearch**: Quick Search Query the Grid : str
    - Optional - Default is None
- **IncludeCount**: Include the Record Count in the Response : bool
    - Optional - Default is True

- **Returns:**
    - If IncludeCount is True:
        - {"count": int, "data": list}
    - If IncludeCount is False:
        - data : list