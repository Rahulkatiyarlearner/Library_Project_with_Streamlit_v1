from data.member_database import member_database


class member_services:

    @staticmethod
    def validation(in_name):

        if len(in_name.strip()) != 0:
            md = member_database()
            get_max_id = md.chk_max_id()
            if get_max_id is None or get_max_id[0] is None:
                max_id = 10000000
            else:
                max_id = get_max_id[0] + 1
            md.enter_member(max_id,in_name)
            ret_data = "Member added in Library. Member id is - " + str(max_id)
            return ret_data
        else:
            return "Name Not Entered Properly"


    @staticmethod
    def ret_usr_list():
        md = member_database()
        out_mem_list = md.load_users()
        mem_list = [out_mem[0] for out_mem in out_mem_list]
        return mem_list


    @staticmethod
    def get_usr_name(in_id):
        md = member_database()
        usr_name = md.chk_id(in_id)
        return usr_name[0]









     







