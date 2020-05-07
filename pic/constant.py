import const

#系统
const.SYS_LANG = 'utf-8'
const.SYS_APPLICATION_EXCEL = 'Excel.Application'
const.SYS_WIN_PROTOCOL = 'WM_DELETE_WINDOW'

const.SYS_CLICK_LEFT = 'left'
const.SYS_CLICK_RIGHT = 'right'
const.SYS_CLICK_DOWN = 'down'
const.SYS_CLICK_UP = 'up'
const.SYS_CLICK_ENTER = 'enter'
const.SYS_KEY_SHIFT = 'shift'
const.SYS_KEY_ALT = 'alt'
const.SYS_KEY_CONTROL = 'ctrl'
const.SYS_KEY_A = 'a'
const.SYS_KEY_B = 'b'
const.SYS_KEY_C = 'c'
const.SYS_KEY_F = 'f'
const.SYS_KEY_W = 'w'

const.SYS_NUM_0 = 0
const.SYS_NUM_1 = 1
const.SYS_NUM_2 = 2
const.SYS_NUM_3 = 3
const.SYS_NUM_4 = 4
const.SYS_NUM_5 = 5
const.SYS_NUM_6 = 6
const.SYS_NUM_8 = 8
const.SYS_NUM_10 = 10
const.SYS_NUM_12 = 12
const.SYS_NUM_14 = 14
const.SYS_NUM_16 = 16
const.SYS_NUM_20 = 20
const.SYS_NUM_24 = 24
const.SYS_NUM_32 = 32
const.SYS_NUM_30 = 30
const.SYS_NUM_36 = 36
const.SYS_NUM_40 = 40
const.SYS_NUM_50 = 50
const.SYS_NUM_70 = 70
const.SYS_NUM_80 = 80
const.SYS_NUM_90 = 90
const.SYS_NUM_100 = 100
const.SYS_NUM_145 = 145
const.SYS_NUM_150 = 150
const.SYS_NUM_160 = 160
const.SYS_NUM_200 = 200
const.SYS_NUM_230 = 230
const.SYS_NUM_025 = 0.25

const.SYS_B_SHOWELL = 'showell'
const.SYS_B_TRUE = True
const.SYS_B_FALSE = False
const.SYS_B_NONE = None
const.SYS_B_POINT = '.'
const.SYS_B_EQUAL = '='
const.SYS_B_COMMA = ','
const.SYS_B_EMPTY = ''
const.SYS_B_UNDERLINE = '_'
const.SYS_B_LINEFEED = '\n'
const.SYS_B_BACKSLACH = '/'
const.SYS_B_SPACE = " "
const.SYS_B_SLACH_2 = '\\'
const.SYS_B_SLACH_4 = '\\\\'
const.SYS_B_CURVES_LEFT = '('
const.SYS_B_CURVES_RIGHT = ')'
const.SYS_B_M_CURVES_LEFT = '['
const.SYS_B_M_CURVES_RIGHT = ']'
const.SYS_B_ALL = '全部'
const.SYS_B_DE = '的'

const.SYS_EXCEL_A1 = "A1"
const.SYS_EXCEL_SHEET1 = "Sheet1"

const.SYS_BACKEND_UIA = 'uia' 

const.RPA_CTRL_TPYE_WINDOW = 'Window'
const.RPA_CTRL_TPYE_BUTTON = 'Button'
const.RPA_CTRL_TPYE_EDIT = 'Edit'
const.RPA_CTRL_TPYE_PANE = 'Pane'
const.RPA_CTRL_TPYE_COMBOBOX = 'ComboBox'
const.PRA_CTRL_TYPE_TREE = 'Tree'

#INI文件
const.INI_PATH = 'rpa.ini'
const.INI_LOGININFO = 'LoginInfo'
const.INI_LOGININFO_OPERATOR = 'operator'
const.INI_LOGININFO_PSD = 'psd'
const.INI_LOGININFO_APPPATH = 'apppath'
const.INI_CODE = 'code'
const.INI_KEY = 'key'

const.INI_ACCOUNTINFO = 'AccountInfo'
const.INI_ACCOUNT = 'account'
const.INI_STAIRWAY = 'stairway'

const.INI_FILEPATH = 'FilePath'
const.INI_FILEPATH_OPENPATH = 'defaultOpenPath'
const.INI_FILEPATH_TEMPFILE = 'doingTemplateFile'
const.INI_FILEPATH_TEMPFILE_IMPORT = 'importTemplateFile'
const.INI_FILEPATH_IMPORTFILE = 'importFile'

const.INI_DOING = 'DoingBomFile'
const.INI_DOING_FILEHEAD = 'doingFileHead'
const.INI_DOING_CLASSIFYSHEET = 'classifySheet'
const.INI_DOING_TITLEROW = 'titleRow'
const.INI_DOING_NAMECOLUMN = 'nameColumn'
const.INI_DOING_SIZECOLUMN = 'sizeColumn'
const.INI_DOING_MATERIALCOLUMN = 'materialColumn'
const.INI_DOING_COLORCOLUMN = 'colorColumn'
const.INI_DOING_AUTO_MATERIAL_LIST = 'materialAutoList'
const.INI_DOING_AUTO_MATERIAL_CLASSIFY = 'materialAutoClassify'
const.INI_DOING_FILE_COLUMN_MAX = 6
const.INI_DOING_REMOTE_FLAG='bom'
const.INI_DOING_REMOTE = 'remote'
const.INI_DOING_PATTERN ='pattern'
const.INI_DOING_PATTERN_COLUMN ='pattern_column'
const.INI_DOING_PATTERN_READY ='pattern_ready'

const.INI_IMPORT = 'ImportBomFile'
const.INI_IMPORT_SHEETTITLE = 'tmpSheetTitle'
const.INI_IMPORT_SHEETCODE = 'sheetCode'

const.INI_TK_Main = 'TKMain'
const.INI_TK_ROOT_TITLE = 'tkroottitle'
const.INI_TK_ROOT_WIDTH = 'tkrootwidth'
const.INI_TK_ROOT_HEIGHT = 'tkrootheight'
const.INI_TK_ICO = 'tkico'
const.INI_MAIN_WIN_TITLE = 'mainwintitle'
const.INI_TK_BACKDOOR = 'backdoor'

const.TK_BACKDOOR_INI_OK = 'ini文件上传完成'
const.TK_BACKDOOR_INI_NG  = 'ini文件上传失败'
const.TK_BACKDOOR_SHOT_OK = 'SHOT上传完成'
const.TK_BACKDOOR_SHOT_NG  = 'SHOT上传失败'
#tkinter
#const.TK_ROOT_TITLE = '索威尔RPA机器人'
const.TK_ROOT_TITLE_OFFLINE = "索威尔RPA机器人_下线中"
const.TK_ROOT_CHOOSE_LABEL = '请选择自动化流程'
const.TK_ROOT_CHOOSE_LABEL_FONT = '微软雅黑 -16'
const.TK_ROOT_FUNCTION_LABEL_FONT = '微软雅黑 -14'
#const.TK_ROOT_WIDTH = 420
#const.TK_ROOT_HEIGHT = 260
const.TK_ROOT_WIN_SIZE_VAR = '%dx%d+%d+%d'
const.TK_ROOT_BTN_BG = '#FFF8DC'
const.TK_ROOT_BTN_EXIT = '退出'
const.TK_ROOT_BTN_SHOWCODE = '查看CODE'
const.TK_ROOT_BTN_INI = 'INI↑'
const.TK_ROOT_BTN_SHOT = 'SHOT↑'
const.TK_ROOT_BTN_SHOT_D = 'SHOT↓'
const.TK_ROOT_BTN_CLASSIFYCODE = '分类编号'
const.TK_ROOT_BTN_EXIT_FONT = '黑体 -14'
const.TK_ROOT_BTN_EXIT_PIC = 'exit.png'
const.TK_ROOT_NOTICE_LABEL_FG = '#2F4F4F'
const.TK_ROOT_WELCOME = '选择上面的流程，开始RPA流程自动化'
const.TK_BOT_OFFLINE = '当前机器人处于下线状态，上线请联系服务商'
const.TK_B_TEXT = 'text'
const.TK_B_STATE = 'state'
const.TK_B_LENGTH = 'length'
const.TK_B_NORMAL = 'normal'
const.TK_B_DISABLED = 'disabled'
const.TK_PROCESSBAR = 'indeterminate'

#const.TK_ICO = 'logo.ico'

const.TK_RPA_1 = '更新分类'
const.TK_RPA_1_START = '更新分类开始'
const.TK_RPA_1_END = '更新分类完成'
const.TK_RPA_2 = 'BOM表单解析'
const.TK_RPA_2_START = 'BOM表单开始解析'
const.TK_RPA_2_END = '表单解析完成，可以开始填写分类及编号'
const.TK_RPA_3 = 'BOM导入'
const.TK_RPA_3_START = 'BOM导入数据准备'
const.TK_RPA_3_Phase_1 = '数据准备完成，开始进行导入'
const.TK_RPA_3_END = 'BOM导入完成'

#登录界面
const.LOGIN_WIN_TITLE = '登陆界面'
const.LOGIN_USER_EDIT_AUTOID = 'txtUser'
const.LOGIN_PSD_EDIT_AUTOID = 'fpass'
const.LOGIN_OK_BTN_AUTOID = 'button1'

#选择帐套界面
const.ACCOUNT_WIN_TITLE = '选择帐套'
const.ACCOUNT_OK_BTN_PIC = 'pic\\account_ok.png'
const.ACCOUNT_CHOOSE = 'pic\\account_choose.png'

#主菜单界面
#const.MAIN_WIN_TITLE = '主菜单 （操作员：管理员）------己启用  版本：V4.62'
const.MAIN_WIN_AUTOID = 'MainForm'
const.MAIN_TREE_AUTOID = 'treeView1'
const.MAIN_IMPORT_BTN_PIC = 'pic\\import_button.png'
const.MAIN_RECOVER_BTN_PIC = 'pic\\import_recover.png'
const.MAIN_CLASSIFY_ALL_PIC = 'pic\\classify_all.png'
const.MAIN_CLASSIFY_ALL_SELECT_PIC = 'pic\\classify_all_selected.png'


#导入界面
const.IMPORT_OPENDATA_BTN_PIC = 'pic\\openresource_button.png'
const.IMPORT_BELONG_LABEL_PIC = 'pic\\import_belong.png'
const.IMPORT_SHEET_LABEL_PIC = 'pic\\import_sheet.png'
const.IMPORT_CONFIRM_BTN_PIC ='pic\\import_confirm.png'
const.IMPORT_FINISH_BTN_PIC = 'pic\\import_finish.png'
const.IMPORT_IMPORT_PANEL_AUTOID = 'panel1'
const.IMPORT_OK_BTN_AUTOID = 'button2'
const.IMPORT_CLOSE_BTN_AUTOID = 'button3'

const.IMPORT_SHEET_CLASSIFY_NAME = '隶属分类'
const.IMPORT_SHEET_GOODS_CODE = '货品编号'
const.IMPORT_SHEET_GOODS_NAME = '货品名称'
const.IMPORT_SHEET_PRODUCT_CODE = '产品型号'
const.IMPORT_SHEET_CLIENT_CODE = '客户型号'
const.IMPORT_SHEET_GOODS_SIZE = '规格'

const.IMPORT_DIAL_TITLE = "选择BOM分类文件"
const.DOING_DIAL_TITLE = "选择BOM文件"

#打开文件选择界面
const.OPEN_WIN_TITLE = '打开'
const.OPEN_FILE_TITLE = '文件名(N):'
const.OPEN_FILE_AUTOID = '1148'
const.OPEN_OPEN_BTN_TITLE = '打开(O)'
const.OPEN_OPEN_BTN_AUTOID = '1'

#类型定义界面
const.DEFINE_WIN_TITLE = '类型定义'
const.DEFINE_WIN_AUTOID = 'Class_Setup'
const.DEFINE_FRONT_BTN_TITLE = '前一记录(P)'
const.DEFINE_FRONT_BTN_AUTOID = 'button1'
const.DEFINE_BELONG_COMBO_AUTOID = 'comboBox1'
const.DEFINE_CODE_EDIT_AUTOID = 'textBox1'
const.DEFINE_NAME_EDIT_AUTOID = 'textBox2'
const.DEFINE_NUM_EDIT_AUTOID = 'textBox3'
const.DEFINE_CLOSE_BTN_AUTOID = 'button4'

#消息
const.ERR_EMPTY_APPPATH = "没有设置APP路径"
const.ERR_EMPTY_FILE_BOMTEMP = "没有设置Bom模板文件"
const.ERR_EMPTY_FILE_BOMDOING = "没有设置Bom doing文件"
const.ERR_EMPTY_SHEETTITLE_CLASSIFY = "没有设置分类Sheet名"

#日志
const.LOG_BOT_START = "[开始]-BOT界面"
const.LOG_BOT_END = "[结束]-BOT界面"
const.LOG_RPA1_START = "[开始]-更新分类"
const.LOG_RPA1_END = "[结束]-更新分类"
const.LOG_RPA1_ERR = "[ERR]-更新分类失败"
const.LOG_RPA2_START = "[开始]-BOM解析"
const.LOG_RPA2_END = "[结束]-BOM解析"
const.LOG_RPA2_ERR = "[ERR]-BOM解析失败"
const.LOG_RPA3_START = "[开始]-BOM导入"
const.LOG_RPA3_END = "[结束]-BOM导入"
const.LOG_RPA3_ERR = "[ERR]-BOM导入失败"
const.LOG_INI_OK = "[OK]-INI上传"
const.LOG_INI_ERR = "[ERR]-INI上传"
const.LOG_INI_DO = "[执行]-INI下载"
const.LOG_INI_ERROR = "[ERR]-INI配置文件错误"
const.LOG_SHOT_OK = "[OK]-SHOT上传"
const.LOG_SHOT_ERR = "[ERR]-SHOT上传"
const.LOG_AUTH_DO = "[执行]-BOT验证"
const.LOG_R_BOM_DO = "[执行]远程读取BOM"
const.LOG_BACKDOOR_DO = "[使用]-实施后门-"



const.LOG_S_0 = "0" #结束
const.LOG_S_1 = "1" #开始
const.LOG_S_2 = "2" #执行中

#功能       
const.LOG_S_00 = "00" #00:自动机器人界面
const.LOG_S_01 = "01" #01:更新分类编号
const.LOG_S_02 = "02" #02:Bom解析
const.LOG_S_03 = "03" #03:Bom导入
const.LOG_S_04 = "04" #03:ini下载

const.LOG_S_11 = "11" #11:ini上传
const.LOG_S_12 = "12" #12:远程remote
const.LOG_S_13 = "13" #13:shot上传
const.LOG_S_97 = "97" #97:退役下线
const.LOG_S_98 = "98" #98:打开后门
const.LOG_S_99 = "99" #99:bot验证


#机器人
const.BOT_CODE = '160323d5eb81470a71e184970b2b6f29'
const.BOT_KEY = 'Cc2+1d2Rv32GSK0zOGD9AQ=='
const.BOT_NAME = '索威尔#9'