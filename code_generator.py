#coding: utf-8

tab = ' '*4
sp = ' '
header_coding = "#coding: utf-8"
def func_gen(name, *args, **kwargs):
    code = [header_coding]
    params = list(args)
    quote = lambda x: x.join(("'", "'"))
    params.extend(['='.join((key, quote(value))) for key, value in kwargs.items()])

    glued_params = ', '.join(params)
    func_name = ')'.join(('('.join((name, glued_params)), ':'))
    func_header = sp.join(('def', func_name))
    code.append(func_header)
    suite = [sp.join((''.join((tab, 'print')), param)) for param in params]
    code.extend(suite)
    gen_file(code, name)
    print params

def gen_file(code, func_name):
    file_name = '.'.join((func_name, 'py'))
    with open(file_name, 'w') as f:
        for line in code:
            f.write(line)
            f.write('\n')

if __name__ == "__main__":
    func_gen('foo', 'name', gender='male')

