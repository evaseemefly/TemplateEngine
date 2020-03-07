class Template:
    '''
        模板类(原型类)
    '''

    def func_1(self):
        print('调用方法1')
        return '无风'

    def func_2(self):
        print('调用方法2')
        return 28.5

    def conver_template(self, funcs={}, **kwargs):

        template = f'''
                    今天天气很好{funcs.get('func_1')()},气温{funcs.get('func_2')()}
                 '''
        return template

    def convert_res(self):
        '''
            将当前类中的其他全部方法
        :return:
        '''
        funcs = ['func_1', 'func_2']
        funcs_dict = {}
        funcs_instance = dir(self)
        for temp in funcs:
            if hasattr(self, temp):
                funcs_dict[temp] = getattr(self, temp)
        print(self.conver_template(funcs_dict))
        pass


def main():
    template = Template()
    template.convert_res()
    pass


if __name__ == '__main__':
    main()
