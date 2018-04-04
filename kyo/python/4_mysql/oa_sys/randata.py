#!/usr/bin/env python3


from random import choice, randint


class randData:

    def getCity(self):
        sql = """ select replace(city_name, '市', '') as city
                  from position.city where city_name like '%市';"""
        return self.getList(sql)

    def getIdList(self, table, con='1'):
        sql = 'select id from %s where state=0 and %s' % (table, con)
        return self.getList(sql)

    def getSid(self):
        return self.getIdList('school')

    def randSid(self, sid=None):
        """
        随机选取一个学校ID
        参数sid控制临时指定随机范围
        """
        if sid is None:
            sid = self.sid
        else:
            sid = sid if isinstance(sid, (list, tuple)) else [sid]
        return choice(sid)

    def getAddTime(self, table, rid):
        """
        获取随机数据的添加时间
        """
        return self.db.col('select addtime from %s where id=%s' % (table, rid))

    @property
    def cnNum(self):
        return '一二三四五六七八九十';

    @property
    def sub(self):
        return ['小学', '大学', '中学', '职业学院', '师范学院',
                '艺术学院', '体育学院', '医学院', '商学院', '女子学院']

    @property
    def course(self):
        return ['语文', '数学', '英语', '政治', '生物', '化学', '物理',
                '历史', '地理', '几何', '美术', '音乐', '体育', '计算机',
                'PHP', 'Python', 'Java', 'C', 'C++', 'Go', 'Shell',
                'Ruby', 'MySQL', 'HTML', 'CSS', 'JavaScript', 'UI',
                'Django', 'Vim', '测试', '运维', '自动化测试',
                '自动化运维']

    @property
    def first(self):
        return ['何', '朱', '李', '王', '张', '刘', '吴', '赵', '田',
                '马', '司徒', '欧阳', '皇甫', '南宫', '诸葛', '上官']

    @property
    def name(self):
        return ('驰福兴华初震泽震骏濡嘉骏锟天宇嘉彬祜梓轩翰贤凯骞振振骏帆'
                '蔓嘉吉晨强柔辰运鸿运振涛桓鸿谷骏暄震寅祯翰栋运锋腾振祜骞'
                '逸运胤浩驰振星尧哲栋寅振凡蔓寅韦骏烁华瑞延鹏晨锋初栋腾嘉'
                '运驰驰鑫振然潍盛鹏博运峰蔓骏骏胤谛凯振轩信骏斌辰骏骏祥辰'
                '星翱海凡爵尧运驰盛卓强哲斌礼运贤权骏逸嘉文骏星福祯胤日槐'
                '驰运龙睿运轩骏濡辰然鸿振骏桀炳栋震骏辰震骏振')

    @property
    def getName(self):
        name = choice(self.first) + choice(self.name)
        if randint(0, 1):
            name += choice(self.name)
        return name

