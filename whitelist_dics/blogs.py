Whitelist = {
        # Foreign science and technology blog posts 
        'medium':['','com','0.8'],
        'groovypost':['','com/howto','0.8'],       # 电脑技术问题

        'leetcode-cn':['','com/problems','0.8'],   # 乐扣试题区
        'nowcoder':['','com/practice','0.8'],      # 牛客试题区, 与乐扣试题相似，但搜不到
        'github': ['','io','0.8'],                 # 没法 用 @://github.*/* 来表示 .com 和 .io，因为这条规则是有问题的
        'gitee':['','io','0.7'],
        'dev':['','to','0.7'],                     # dev
        'ruanyifeng':['','com','0.65'],            # 阮一峰的网络日志
        'zhihu':['zhuanlan','com','0.6'],          # 知乎专栏
        'liaoxuefeng':['','com/wiki','0.5'],       # 廖雪峰的官方网站
        'coolshell':['','cn/articles','0.5'],      # 酷壳
        'cnblogs':['www','com','0.4'],             # 博客园，加上 www 是为了过滤 https://recomm.cnblogs.com/ 这个地址
        '': ['','edu','0.05'],                     # 所有以 edu 结尾的域名(学校)
}
