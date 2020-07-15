import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import email
import smtplib



'''1 手厅 - 访问活动素材列表'''
# 访问该地址访问需要传入cookies
# cookie = {'Cookie':'index_router=/marketCenter; EntAdminG_STORE={%22menus%22:%22[{%5C%22id%5C%22:1%2C%5C%22path%5C%22:%5C%22home%5C%22%2C%5C%22name%5C%22:%5C%22%E9%A6%96%E9%A1%B5%5C%22%2C%5C%22globalVar%5C%22:%5C%22home%5C%22%2C%5C%22jsPath%5C%22:%5C%22http://statics.jituancaiyun.net/entadmin2/home/0.1.10/index.js%5C%22%2C%5C%22hide%5C%22:false}%2C{%5C%22id%5C%22:2%2C%5C%22path%5C%22:%5C%22contacts%5C%22%2C%5C%22name%5C%22:%5C%22%E9%80%9A%E8%AE%AF%E5%BD%95%5C%22%2C%5C%22globalVar%5C%22:%5C%22contacts%5C%22%2C%5C%22jsPath%5C%22:%5C%22http://statics.jituancaiyun.net/entadmin2/contacts/0.0.1/index.js%5C%22}%2C{%5C%22id%5C%22:382%2C%5C%22path%5C%22:%5C%22personnel%5C%22%2C%5C%22name%5C%22:%5C%22%E5%91%98%E5%B7%A5%E7%AE%A1%E7%90%86%5C%22%2C%5C%22globalVar%5C%22:%5C%22personnel%5C%22%2C%5C%22jsPath%5C%22:%5C%22http://statics.jituancaiyun.net/entadmin2/personnel/0.0.1/index.js%5C%22}%2C{%5C%22id%5C%22:7%2C%5C%22path%5C%22:%5C%22application%5C%22%2C%5C%22name%5C%22:%5C%22%E4%BC%81%E4%B8%9A%E5%BA%94%E7%94%A8%5C%22%2C%5C%22globalVar%5C%22:%5C%22application%5C%22%2C%5C%22jsPath%5C%22:%5C%22http://statics.jituancaiyun.net/entadmin2/application/0.0.7/index.js%5C%22%2C%5C%22iframe%5C%22:false}%2C{%5C%22id%5C%22:17%2C%5C%22path%5C%22:%5C%22entservice%5C%22%2C%5C%22name%5C%22:%5C%22%E4%BC%81%E4%B8%9A%E6%9C%8D%E5%8A%A1%5C%22%2C%5C%22globalVar%5C%22:%5C%22entservice%5C%22%2C%5C%22jsPath%5C%22:%5C%22http://admin.jituancaiyun.net/entpay/htmls/account/index.html%5C%22%2C%5C%22iframe%5C%22:true}%2C{%5C%22id%5C%22:19%2C%5C%22path%5C%22:%5C%22setup%5C%22%2C%5C%22name%5C%22:%5C%22%E6%88%91%E7%9A%84%E4%BC%81%E4%B8%9A%5C%22%2C%5C%22globalVar%5C%22:%5C%22setup%5C%22%2C%5C%22jsPath%5C%22:%5C%22http://statics.jituancaiyun.net/entadmin2/setup/0.0.4/index.js%5C%22}]%22%2C%22entServiceUrl%22:%22http://admin.jituancaiyun.net/entpay/htmls/account/index.html%22%2C%22isEntAdmin%22:2%2C%22orgId%22:%2289441%22%2C%22orgName%22:%22%E6%B5%8B%E8%AF%95%E4%BC%81%E4%B8%9A19%22%2C%22name%22:%22%E9%99%88%E5%87%AF%E4%B8%BD%22%2C%22mobile%22:%2218850583991%22%2C%22superAdmin%22:0%2C%22superMobile%22:%22null%22%2C%22subOrg%22:false%2C%22teamOrg%22:false%2C%22uid%22:%22101010013986609%22%2C%22industryVersionType%22:%220%22}; userName=%E7%8E%8B%E8%80%85; _scn=cea4c2e4Mff65c3ceM170a9c0374fM7af7; uiapp=%7B%22orgId%22%3A%2289441%22%2C%22orgName%22%3A%22%E6%B5%8B%E8%AF%95%E4%BC%81%E4%B8%9A19%22%2C%22name%22%3A%22%E9%99%88%E5%87%AF%E4%B8%BD%22%2C%22mobile%22%3A%2218850583991%22%2C%22superAdmin%22%3A0%2C%22superMobile%22%3A%22null%22%2C%22subOrg%22%3Afalse%2C%22teamOrg%22%3Afalse%2C%22uid%22%3A%22101010013986609%22%2C%22industryVersionType%22%3A%220%22%7D; userId=101010013625688; token=7cf3d22ef5da64c8b1588b86f9d82892; timeStamp=1583490166065856; mobile=18822222222; sessionId=6801038476509214770; _NOWUID=101010013625688; isLogined=1'}

# 直接使用URL参数
# r = requests.get('http://cmmc.jituancaiyun.net/yxzx-opr/material/list.json?_=1583920335756&level=2&status=158&id=1938&pageIndex=1&pageSize=20', cookies = cookie, verify = False)
# # 也可以直接用params传数
# # r = requests.get('https://hao.360.com/?src=bm', params={'cookie': '******'})
#
# # 查看接口返回码
# print(r.status_code)

# 将返回结果json化
# response = r.json()
# print(response)
#
# # 从返回结果中取具体的某个值，注意不同的数据结构（字典key、列表下标）取值方式不同
# print(response['data'])
# print(response['success'])
# print(response['data']['list'])
# print(response['data']['list'][0])
# print(response['data']['list'][0]['id'])
# print(r.raise_for_status())





'''杂记'''
# print(r.json())
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
# print(r.request)
# print(r.encoding)
# r.encoding = 'ISO-8859-1'
# print(r.encoding)
# h = r.headers
# print(h)
# for k, v in h.items():
#     print(k, ':', v)



'''2 手厅 - 新增/修改泛渠道账号信息'''

# url2 = "http://cmmc.jituancaiyun.net/yxzx-opr/permission/channel/saveAndUpdate"

# 入参数据
# params2 = {
#      'id': '5717888926',
#      'channelNumber': '18850583991',
#      'channelName': 'ckl测试泛渠道222',
#      'regionCode': '330101',
#      'channelLeaderName': '荔枝味爸爸3333',
#      'channelLeaderMobile': '18866666666',
#      'type': '1',
#     }

# 请求头，必须要有cookie，不然报错：token check error
# header = {
#     'Content-Type': 'application/json',
#     'cookie': 'index_router=/marketCenter; EntAdminG_STORE={%22menus%22:%22[{%5C%22id%5C%22:1%2C%5C%22path%5C%22:%5C%22home%5C%22%2C%5C%22name%5C%22:%5C%22%E9%A6%96%E9%A1%B5%5C%22%2C%5C%22globalVar%5C%22:%5C%22home%5C%22%2C%5C%22jsPath%5C%22:%5C%22http://statics.jituancaiyun.net/entadmin2/home/0.1.10/index.js%5C%22%2C%5C%22hide%5C%22:false}%2C{%5C%22id%5C%22:2%2C%5C%22path%5C%22:%5C%22contacts%5C%22%2C%5C%22name%5C%22:%5C%22%E9%80%9A%E8%AE%AF%E5%BD%95%5C%22%2C%5C%22globalVar%5C%22:%5C%22contacts%5C%22%2C%5C%22jsPath%5C%22:%5C%22http://statics.jituancaiyun.net/entadmin2/contacts/0.0.1/index.js%5C%22}%2C{%5C%22id%5C%22:382%2C%5C%22path%5C%22:%5C%22personnel%5C%22%2C%5C%22name%5C%22:%5C%22%E5%91%98%E5%B7%A5%E7%AE%A1%E7%90%86%5C%22%2C%5C%22globalVar%5C%22:%5C%22personnel%5C%22%2C%5C%22jsPath%5C%22:%5C%22http://statics.jituancaiyun.net/entadmin2/personnel/0.0.1/index.js%5C%22}%2C{%5C%22id%5C%22:7%2C%5C%22path%5C%22:%5C%22application%5C%22%2C%5C%22name%5C%22:%5C%22%E4%BC%81%E4%B8%9A%E5%BA%94%E7%94%A8%5C%22%2C%5C%22globalVar%5C%22:%5C%22application%5C%22%2C%5C%22jsPath%5C%22:%5C%22http://statics.jituancaiyun.net/entadmin2/application/0.0.7/index.js%5C%22%2C%5C%22iframe%5C%22:false}%2C{%5C%22id%5C%22:17%2C%5C%22path%5C%22:%5C%22entservice%5C%22%2C%5C%22name%5C%22:%5C%22%E4%BC%81%E4%B8%9A%E6%9C%8D%E5%8A%A1%5C%22%2C%5C%22globalVar%5C%22:%5C%22entservice%5C%22%2C%5C%22jsPath%5C%22:%5C%22http://admin.jituancaiyun.net/entpay/htmls/account/index.html%5C%22%2C%5C%22iframe%5C%22:true}%2C{%5C%22id%5C%22:19%2C%5C%22path%5C%22:%5C%22setup%5C%22%2C%5C%22name%5C%22:%5C%22%E6%88%91%E7%9A%84%E4%BC%81%E4%B8%9A%5C%22%2C%5C%22globalVar%5C%22:%5C%22setup%5C%22%2C%5C%22jsPath%5C%22:%5C%22http://statics.jituancaiyun.net/entadmin2/setup/0.0.4/index.js%5C%22}]%22%2C%22entServiceUrl%22:%22http://admin.jituancaiyun.net/entpay/htmls/account/index.html%22%2C%22isEntAdmin%22:2%2C%22orgId%22:%2289441%22%2C%22orgName%22:%22%E6%B5%8B%E8%AF%95%E4%BC%81%E4%B8%9A19%22%2C%22name%22:%22%E9%99%88%E5%87%AF%E4%B8%BD%22%2C%22mobile%22:%2218850583991%22%2C%22superAdmin%22:0%2C%22superMobile%22:%22null%22%2C%22subOrg%22:false%2C%22teamOrg%22:false%2C%22uid%22:%22101010013986609%22%2C%22industryVersionType%22:%220%22}; userName=%E7%8E%8B%E8%80%85; _scn=cea4c2e4Mff65c3ceM170a9c0374fM7af7; uiapp=%7B%22orgId%22%3A%2289441%22%2C%22orgName%22%3A%22%E6%B5%8B%E8%AF%95%E4%BC%81%E4%B8%9A19%22%2C%22name%22%3A%22%E9%99%88%E5%87%AF%E4%B8%BD%22%2C%22mobile%22%3A%2218850583991%22%2C%22superAdmin%22%3A0%2C%22superMobile%22%3A%22null%22%2C%22subOrg%22%3Afalse%2C%22teamOrg%22%3Afalse%2C%22uid%22%3A%22101010013986609%22%2C%22industryVersionType%22%3A%220%22%7D; channel_id=5717888900; regionCode=330100; userId=101010013625688; token=77922e7a8843da6e14b61209919226a3; timeStamp=1584346669086856; mobile=18822222222; sessionId=6804717128884992253; _NOWUID=101010013625688; isLogined=1',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
#     }

# res = requests.post(url=url2, json=params2, headers=header, verify=False)
# 返回结果json化
# print(res.json())
# print(res.raise_for_status())





'''3 手厅 - 删除泛渠道账号信息'''
# url3 = 'http://cmmc.jituancaiyun.net/yxzx-opr/permission/channel/delete?id=5717888931'

# header = {
#     'Content-Type': 'application/json',
#     'cookie': 'index_router=/marketCenter; EntAdminG_STORE={%22menus%22:%22[{%5C%22id%5C%22:1%2C%5C%22path%5C%22:%5C%22home%5C%22%2C%5C%22name%5C%22:%5C%22%E9%A6%96%E9%A1%B5%5C%22%2C%5C%22globalVar%5C%22:%5C%22home%5C%22%2C%5C%22jsPath%5C%22:%5C%22http://statics.jituancaiyun.net/entadmin2/home/0.1.10/index.js%5C%22%2C%5C%22hide%5C%22:false}%2C{%5C%22id%5C%22:2%2C%5C%22path%5C%22:%5C%22contacts%5C%22%2C%5C%22name%5C%22:%5C%22%E9%80%9A%E8%AE%AF%E5%BD%95%5C%22%2C%5C%22globalVar%5C%22:%5C%22contacts%5C%22%2C%5C%22jsPath%5C%22:%5C%22http://statics.jituancaiyun.net/entadmin2/contacts/0.0.1/index.js%5C%22}%2C{%5C%22id%5C%22:382%2C%5C%22path%5C%22:%5C%22personnel%5C%22%2C%5C%22name%5C%22:%5C%22%E5%91%98%E5%B7%A5%E7%AE%A1%E7%90%86%5C%22%2C%5C%22globalVar%5C%22:%5C%22personnel%5C%22%2C%5C%22jsPath%5C%22:%5C%22http://statics.jituancaiyun.net/entadmin2/personnel/0.0.1/index.js%5C%22}%2C{%5C%22id%5C%22:7%2C%5C%22path%5C%22:%5C%22application%5C%22%2C%5C%22name%5C%22:%5C%22%E4%BC%81%E4%B8%9A%E5%BA%94%E7%94%A8%5C%22%2C%5C%22globalVar%5C%22:%5C%22application%5C%22%2C%5C%22jsPath%5C%22:%5C%22http://statics.jituancaiyun.net/entadmin2/application/0.0.7/index.js%5C%22%2C%5C%22iframe%5C%22:false}%2C{%5C%22id%5C%22:17%2C%5C%22path%5C%22:%5C%22entservice%5C%22%2C%5C%22name%5C%22:%5C%22%E4%BC%81%E4%B8%9A%E6%9C%8D%E5%8A%A1%5C%22%2C%5C%22globalVar%5C%22:%5C%22entservice%5C%22%2C%5C%22jsPath%5C%22:%5C%22http://admin.jituancaiyun.net/entpay/htmls/account/index.html%5C%22%2C%5C%22iframe%5C%22:true}%2C{%5C%22id%5C%22:19%2C%5C%22path%5C%22:%5C%22setup%5C%22%2C%5C%22name%5C%22:%5C%22%E6%88%91%E7%9A%84%E4%BC%81%E4%B8%9A%5C%22%2C%5C%22globalVar%5C%22:%5C%22setup%5C%22%2C%5C%22jsPath%5C%22:%5C%22http://statics.jituancaiyun.net/entadmin2/setup/0.0.4/index.js%5C%22}]%22%2C%22entServiceUrl%22:%22http://admin.jituancaiyun.net/entpay/htmls/account/index.html%22%2C%22isEntAdmin%22:2%2C%22orgId%22:%2289441%22%2C%22orgName%22:%22%E6%B5%8B%E8%AF%95%E4%BC%81%E4%B8%9A19%22%2C%22name%22:%22%E9%99%88%E5%87%AF%E4%B8%BD%22%2C%22mobile%22:%2218850583991%22%2C%22superAdmin%22:0%2C%22superMobile%22:%22null%22%2C%22subOrg%22:false%2C%22teamOrg%22:false%2C%22uid%22:%22101010013986609%22%2C%22industryVersionType%22:%220%22}; userName=%E7%8E%8B%E8%80%85; _scn=cea4c2e4Mff65c3ceM170a9c0374fM7af7; uiapp=%7B%22orgId%22%3A%2289441%22%2C%22orgName%22%3A%22%E6%B5%8B%E8%AF%95%E4%BC%81%E4%B8%9A19%22%2C%22name%22%3A%22%E9%99%88%E5%87%AF%E4%B8%BD%22%2C%22mobile%22%3A%2218850583991%22%2C%22superAdmin%22%3A0%2C%22superMobile%22%3A%22null%22%2C%22subOrg%22%3Afalse%2C%22teamOrg%22%3Afalse%2C%22uid%22%3A%22101010013986609%22%2C%22industryVersionType%22%3A%220%22%7D; channel_id=5717888900; regionCode=330100; userId=101010013625688; token=77922e7a8843da6e14b61209919226a3; timeStamp=1584346669086856; mobile=18822222222; sessionId=6804717128884992253; _NOWUID=101010013625688; isLogined=1',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
#    }
# res = requests.post(url=url3, headers=header, verify=False)
# print(res.json())



'''4 手厅 - 上传目标用户名单'''
# url4 = 'https://cmmc.jituancaiyun.com/yxzx-opr/whitelist/upload.json'
# header = {
#      'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryByCuNqZYwYBkxwgh',
#      'cookie': 'index_router=/marketCenter; userName=%E9%99%88%E5%87%AF%E4%B8%BD; _scn=2942ba7eSb5c6a335S1709e52a4f4Sf574; acw_tc=2760829515837377168707625e081518d779b8783e44cc8ddd3d6ef1da2707; channel_id=5717888904; regionCode=-1; userId=10101001201781200; mobile=18850583991; sessionId=6804707864868578442; _NOWUID=10101001201781200; token=b8abb397bc0ee3964731165988f8c0c1; timeStamp=1584440915135055; isLogined=1',
#      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
#     }
# file = {
#     'file': ('upload', open('/Users/chenkaili/Downloads/reupload1.xlsx', 'rb'), 'multipart/form-data')
#  }
# # params = {
# #     'multipartFile': 'reupload1.xlsx',
# #     'listType': '1'
# # }
# res = requests.post(url=url4, headers=header,  files=file, verify=False)
# print(res.json())




'''5 手厅- 活动素材上传图片'''
# url5= 'https://cmmc.jituancaiyun.com/sfs/webUpload/file'
# header = {
#      'Content-Type': 'application/json',
#      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
#      'cookie': 'index_router=/marketCenter; userName=%E9%99%88%E5%87%AF%E4%B8%BD; _scn=2942ba7eSb5c6a335S1709e52a4f4Sf574; acw_tc=2760829515837377168707625e081518d779b8783e44cc8ddd3d6ef1da2707; channel_id=5717888904; regionCode=-1; userId=10101001201781200; mobile=18850583991; sessionId=6804707864868578442; _NOWUID=10101001201781200; token=b8abb397bc0ee3964731165988f8c0c1; timeStamp=1584440915135055; isLogined=1'
#     }
#
# file = {
#     'file': open('/Users/chenkaili/Downloads/活动图片/缩略.png', 'rb')
# }
# res = requests.post(url=url5, headers=header, files=file, verify=False)
# print(res.json())



'''6 session保持会话 ，跨请求保持参数headers、cookies等'''
# s = requests.Session()
# s.auth = ('user', 'pass')
# s.headers.update({'y-test': 'true'})
# s.cookies.update({'x-test': 'true'})
# s.cookies.update({'x-text2': 'false'})
#
# 请求方法中的字典数据会与session中设置的数据合并，如果重名则方法层的数据覆盖会话层的数据
# 方法层的数据不会在方法之间保持，只对单个方法有效
# r = s.get('http://httpbin.org/headers', headers={'y-test': 'False', 'y-text2': 'true'})
# r2 = s.get('http://httpbin.org/headers')
# print(r.text)
# print(r2.text)
#
# cookies可以使用set在请求方法中设置会话层的数据，进而在多个方法之间传递
# res = s.get('http://httpbin.org/cookies/set/x-test/None')
# res2 = s.get('http://httpbin.org/cookies')
# print(res.text)
# print(res2.text)


'''7 session保持cookies - saas礼品商后台登录，再访问登录后页面'''
s = requests.session()
url7 = 'http://youli.uban360.net/gift-manager/account/login'
params = {
    'mobile': '18850583991',
    'password': '11111111a'
}
# 登录后台，获得cookie，并在会话对象s中保持
res = s.post(url=url7, data=params)
print(res.json())
# print(res.text)
# print(res.cookies)

# 访问站点列表数据，该数据需要登录才可以访问，用session对象s来访问
# res1 = s.get(url='http://youli.uban360.net/gift-manager/site/list')
# print(res1.json())
# print(res1.cookies)

# 上传商品图片

# url8 = 'http://youli.uban360.net/gift-manager/file/manager/upload'
# file = {
#     'file':open('/Users/chenkaili/Downloads/蛋黄酥1.jpg', 'rb')
# }
# res2 = s.post(url=url8, files=file)
# print(res2.text)