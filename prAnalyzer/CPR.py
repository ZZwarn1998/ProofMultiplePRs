

class CPR:
    def __init__(self, url="", merged=False, more_time_span=0, language="", dev_type="", more_comment_num=0,
                 more_review_comment_num=0, more_commit_num=0, more_add_num=0, more_del_num=0,
                 more_change_file_num=0):
        self.url = url  # pr url
        self.merged = merged    # merged
        self.more_time_span = more_time_span  # time span is more than alternative PR's ？
        self.language = language    # program language
        self.dev_type = dev_type    # developer type
        self.more_comment_num = more_comment_num  # number of comments is more than alternative PR's ？
        self.more_review_comment_num = more_review_comment_num    # number of review comments is more than alternative
        # PR's ？
        self.more_commit_num = more_commit_num    # number of commits is more than alternative PR's ？
        self.more_add_num = more_add_num  # number of added lines is more than alternative PR's ？
        self.more_del_num = more_del_num  # number of deleted lines is more than alternative PR's ？
        self.more_change_file_num = more_change_file_num  # number of changed files is more than alternative PR's ？
    
    def toString(self):
        print(self.url, self.merged, self.language, self.dev_type, self.more_time_span, self.more_comment_num,
              self.more_review_comment_num, self.more_commit_num, self.more_add_num, self.more_del_num, self.more_change_file_num)

    def tolist(self):
        return [self.url, self.merged, self.language, self.dev_type, self.more_time_span, self.more_comment_num,
                self.more_review_comment_num, self.more_commit_num, self.more_add_num, self.more_del_num,
                self.more_change_file_num]


