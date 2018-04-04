#!/usr/bin/env python3


import os
import sys
import codecs
import pickle
from urllib.parse import unquote


sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)


print('Content-Type: text/html; charset=utf-8')
print()

#  for e in os.environ:
    #  print('<h3><span style="color: red">%s</span>: %s</h3>' % (e, os.environ[e]))

def parse_data(qs):
    GET = {}
    if qs:
        for x in qs.split('&'):
            k, v = x.split('=')
            GET[k] = v
    return GET

def stu_list():
    db = open("./data.db", "rb")

    data_list = ""
    while True:
        try:
            data = pickle.load(db)
        except:
            break
        data_list += '<tr>'
        data_list += '<td>%s</td>' % data['name']
        data_list += '<td>%s</td>' % data['age']
        data_list += '<td>%s</td>' % ('男' if data['sex'] == '1' else '女')
        data_list += '</tr>'

    option_list = '<option value="">请选择年龄</option>'
    for i in range(16, 30):
        option_list += '<option value="%s">%s</option>' % (i, i)

    html = """
    <!DOCTYPE html>
    <html lang="zh-CN">
      <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
        <title>Bootstrap 101 Template</title>

        <!-- Bootstrap -->
        <!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
        <link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

        <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
          <script src="https://cdn.bootcss.com/html5shiv/3.7.3/html5shiv.min.js"></script>
          <script src="https://cdn.bootcss.com/respond.js/1.4.2/respond.min.js"></script>
        <![endif]-->
      </head>
      <body>
        <div class="page-header"><h1>学生管理系统</h1></div>
        <div class="container">
            <div class="row" style="margin-bottom: 20px;">
                <div class="col-lg-12">
                    <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#myModal">添加</button>
                </div>
            </div>
            <table class="table table-striped table-bordered">
                <thread>
                <tr>
                    <th>姓名</th>
                    <th>年龄</th>
                    <th>性别</th>
                </tr>
                </thread>
                <tbody>
                {data_list}
                </tbody>
            </table>

            <div class="modal fade" id="myModal" tabindex="-1" role="dialog">
              <div class="modal-dialog" role="document">
                <div class="modal-content">
                <form method="POST">
                  <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                    <h4 class="modal-title">添加学生</h4>
                  </div>
                  <div class="modal-body">
                        <input type="text" name="name" class="form-control" placeholder="学生姓名" style="margin-bottom: 10px;">
                        <label class="radio-inline" style="margin-bottom: 10px">
                            <input type="radio" name="sex" value="1" checked> 男
                        </label>
                        <label class="radio-inline" style="margin-bottom: 10px">
                            <input type="radio" name="sex" value="0"> 女
                        </label>
                        <select name="age" class="form-control">
                            {option_list}
                        </select>
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                    <button type="submit" class="btn btn-primary">添加</button>
                  </div>
                </form>
                </div><!-- /.modal-content -->
              </div><!-- /.modal-dialog -->
            </div><!-- /.modal -->
        </div>

        <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="https://cdn.bootcss.com/jquery/1.12.4/jquery.min.js"></script>
        <!-- Include all compiled plugins (below), or include individual files as needed -->
        <!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
        <script src="https://cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
      </body>
    </html>
    """

    return html.format(option_list=option_list, data_list=data_list)

def stu_add(data):
    #  print("<h1>学生姓名: %s</h1>" % unquote(data.get('name')))
    #  print("<h1>学生年龄: %s</h1>" % data.get('age'))
    #  print("<h1>学生性别: %s</h1>" % ('男' if data.get('sex') == '1' else '女'))
    data['name'] = unquote(data['name'])
    db = open("./data.db", "ab")
    pickle.dump(data, db)


#  if GET.get("op") == 'add':
if os.environ['REQUEST_METHOD'] == 'POST':
    POST = parse_data(input())
    stu_add(POST)
else:
    GET = parse_data(os.environ.get('QUERY_STRING', ''))

print(stu_list())




