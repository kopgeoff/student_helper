def get_semester():
    semester = {'000101': '44', '000102': '43', '010201': '42', '010202': '41',
                '020301': '13', '020302': '14', '030401': '24', '030402': '15',
                '040501': '32', '040502': '16', '050601': '33', '050602': '17',
                '060701': '34', '060702': '18', '070801': '35', '070802': '19',
                '080901': '36', '080902': '20', '091001': '37', '091002': '21',
                '101101': '3', '101102': '22', '111201': '4', '111202': '23',
                '121301': '5', '121302': '25', '131401': '6', '131402': '26',
                '141501': '7', '141502': '2', '141503': '53',
                '151601': '8', '151602': '27', '151603': '52',
                '161701': '9', '161702': '28', '161703': '51',
                '171801': '10', '171802': '29', '171803': '50',
                '181901': '11', '181902': '30', '181903': '49',
                '192001': '12', '192002': '31', '192003': '54',
                '202101': '47', '202102': '48', '202103': '55',
                '212201': '56', '212202': '57', '212203': '58',
                '222301': '59', '222302': '60', '222303': '70',
                '232401': '71', '232402': '72'}
    return semester
# get index of semester
# key值含义，例：192002划分为19，20，02，表示19-20的第二个学期
# 学期划分为：01秋季学期，02春季学期，03夏季学期，建议首先判断key值，避免用户选择没有的学期导致崩溃
