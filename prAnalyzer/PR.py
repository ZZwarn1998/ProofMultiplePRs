

class PR:
    def __init__(self, url="", merged=False, time_span=0, language="", dev_type="", comment_num=0, review_comment_num=0,
                 commit_num=0, add_num=0, del_num=0, change_file_num=0):
        self.url = url  # pr url
        self.merged = merged    # merged
        self.time_span = time_span  # time span
        self.language = language    # program language
        self.dev_type = dev_type    # developer type
        self.comment_num = comment_num  # number of comments
        self.review_comment_num = review_comment_num    # number of review comments
        self.commit_num = commit_num    # number of commits
        self.add_num = add_num  # number of added lines
        self.del_num = del_num  # number of deleted lines
        self.change_file_num = change_file_num  # number of changed files

    def toString(self):
        print(self.url, self.merged, self.time_span, self.language, self.dev_type, self.comment_num,
              self.review_comment_num, self.commit_num, self.add_num, self.del_num, self.change_file_num)
