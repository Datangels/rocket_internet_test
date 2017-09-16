class Link(object):
    def __init__(self, parent_name, child_name):
        self.parent_name = parent_name
        self.child_name = child_name


def find_venture(links, name):
    """
    ​Given​ ​a​ ​list​ ​of​ ​links​ ​and​ ​an​ ​account​ ​name,​ ​finds​ ​the​ ​name​ ​of​ ​the
    venture​ ​it​ ​belongs.​
    :param links: 
    :param name: 
    :return: 
    """
    link = [elem for elem in links if elem.child_name == name][0]
    if link.parent_name == 'Root':
        return link.child_name
    return find_venture(links, link.parent_name)


if __name__ == '__main__':
    l = Link('Root', 'Footpanda')
    r = Link('Root', 'Zalando')
    l_l = Link('Footpanda', 'account1')
    l_r = Link('Footpanda', 'account2')
    r_r = Link('Zalando', 'account3')
    r_r_l = Link('account3', 'account4')
    r_r_r = Link('account3', 'account5')
    r_r_l_l = Link('account4', 'account6')
    r_r_l_l_l = Link('account6', 'account7')
    r_r_l_l_r = Link('account6', 'account8')
    links = [l, r, l_l, l_r, r_r, r_r_l, r_r_r, r_r_l_l, r_r_l_l_l, r_r_l_l_r]
    print find_venture(links, 'account8')

