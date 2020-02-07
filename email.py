my_str='''Lorem ipsum dolor sit amet, consectetur adipiscing 
        elit. Mauris vulputate lacus id eros consequat tempus. 
        Nam viverra velit sit amet lorem lobortis, at tincidunt
        nunc ultricies. Duis facilisis ultrices lacus, id 
        tiger123@email.cz auctor massa molestie at. Nunc tristique 
        fringilla congue. Donec ante diam cnn@info.com, dapibus
        lacinia vulputate vitae, ullamcorper in justo. Maecenas 
        massa purus, ultricies a dictum ut, dapibus vitae massa. 
        Cras abc@gmail.com vel libero felis. In augue elit, porttitor 
        nec molestie quis, auctor a quam. Quisque b2b@money.fr 
        pretium dolor et tempor feugiat. Morbi libero lectus, 
        porttitor eu mi sed, luctus lacinia risus. Maecenas posuere
        leo sit amet spam@info.cz. elit tincidunt maximus. Aliquam 
        erat volutpat. Donec eleifend felis at leo ullamcorper cursus.
        Pellentesque id dui viverra, auctor enim ut, fringilla est. 
        Maecenas gravida turpis nec ultrices aliquet.'''

main_list = my_str.split(' ')
email_num = []
domains = []
final_dic = {}


def all_mails():
    all_email = []
    for i in main_list:
        if '@' in i:
            all_email.append(i)
    #print(all_email)
    return all_email

def get_domain():
    for i in all_mails():
        domain = i.split('@')[1]
        domains.append(domain)
    final_dic['domains'] = domains

def email_with_num():
    for i in all_mails():
        for y in i:
            if y.isdigit():
                email_num.append(i)
                break
    #print(email_num)
    final_dic['emails_with_nums'] = email_num
    #print(final_dic)

# def final_output():
#     get_domain()
#     email_with_num()
#     print(final_dic)

# final_output()

if __name__=='__main__':
    get_domain()
    email_with_num()
    print(final_dic)