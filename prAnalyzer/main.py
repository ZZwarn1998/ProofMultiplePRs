import xlrd
import os
from PR import PR
from CPR import CPR
from collections import Counter
import numpy as np


def read_excel():
    path = os.path.dirname(__file__) + "/data/alternative_prs.xlsx"
    print(os.path.isfile(path))

    wk_bk = xlrd.open_workbook(path)

    merged_pr_sheet = wk_bk.sheet_by_index(0)
    closed_pr_sheet = wk_bk.sheet_by_index(1)

    urls = set()
    url2closed_prs = dict()
    url2merged_prs = dict()

    merged_pr_sheet_rows = merged_pr_sheet.nrows
    merged_pr_sheet_cols = merged_pr_sheet.ncols

    pre_i = 0
    cur_i = 1
    index = 0

    while cur_i < merged_pr_sheet_rows:
        # print(merged_pr_sheet.row_values(cur_i))
        url1 = merged_pr_sheet.row_values(cur_i)[0].strip()
        time_span1 = int(merged_pr_sheet.row_values(cur_i)[3])
        language1 = merged_pr_sheet.row_values(cur_i)[4].strip()
        dev_type1 = merged_pr_sheet.row_values(cur_i)[5].strip()
        comment_num1 = int(merged_pr_sheet.row_values(cur_i)[6])
        review_comment_num1 = int(merged_pr_sheet.row_values(cur_i)[7])
        commit_num1 = int(merged_pr_sheet.row_values(cur_i)[8])
        add_num1 = int(merged_pr_sheet.row_values(cur_i)[9])
        del_num1 = int(merged_pr_sheet.row_values(cur_i)[10])
        change_file_num1 = int(merged_pr_sheet.row_values(cur_i)[11])
        merged_pr = PR(url1, True, time_span1, language1, dev_type1, comment_num1, review_comment_num1, commit_num1,
                       add_num1, del_num1, change_file_num1)

        url2 = closed_pr_sheet.row_values(cur_i)[0].strip()
        time_span2 = int(closed_pr_sheet.row_values(cur_i)[1])
        language2 = "unknown"
        dev_type2 = closed_pr_sheet.row_values(cur_i)[2].strip()
        comment_num2 = int(closed_pr_sheet.row_values(cur_i)[3])
        review_comment_num2 = int(closed_pr_sheet.row_values(cur_i)[4])
        commit_num2 = int(closed_pr_sheet.row_values(cur_i)[5])
        add_num2 = int(closed_pr_sheet.row_values(cur_i)[6])
        del_num2 = int(closed_pr_sheet.row_values(cur_i)[7])
        change_file_num2 = int(closed_pr_sheet.row_values(cur_i)[8])

        closed_pr = PR(url2, False, time_span2, language2, dev_type2, comment_num2, review_comment_num2, commit_num2,
                       add_num2, del_num2, change_file_num2)

        if url1 not in urls:
            urls.add(url1)
            url2closed_pr = {url1: [closed_pr]}
            url2closed_prs.update(url2closed_pr)
            url2merged_pr = {url1: merged_pr}
            url2merged_prs.update(url2merged_pr)
        else:
            url2closed_prs[url1].extend([closed_pr])
        cur_i += 1

    for url in urls:
        if len(url2closed_prs[url])>=2:
            print("-" * 50)
            url2merged_prs[url].toString()
            for i in range(len(url2closed_prs[url])):
                url2closed_prs[url][i].toString()
    
    return urls, url2merged_prs, url2closed_prs


def getCPRs(us, u2m, u2c):
    CPRs = []

    for u in us:
        mpr = u2m[u]
        for i in range(len(u2c[u])):
            cpr = u2c[u][i]
            CPR1, CPR2 = getCPR(mpr, cpr)
            CPRs.extend([CPR1, CPR2])
    return CPRs


def getCPR(mpr, cpr):
    url1 = mpr.url
    merged1 = mpr.merged
    time_span1 = 0 if mpr.time_span - cpr.time_span == 0 \
        else 1 if mpr.time_span - cpr.time_span > 0 \
        else -1
    language1 = mpr.language
    dev_type1 = mpr.dev_type
    comment_num1 = 0 if mpr.comment_num - cpr.comment_num == 0 \
        else 1 if mpr.comment_num - cpr.comment_num > 0 \
        else -1
    review_comment_num1 = 0 if mpr.review_comment_num - cpr.review_comment_num == 0 \
        else 1 if mpr.review_comment_num - cpr.review_comment_num > 0 \
        else -1
    commit_num1 = 0 if mpr.commit_num - cpr.commit_num == 0 \
        else 1 if mpr.commit_num - cpr.commit_num > 0 \
        else -1
    add_num1 = 0 if mpr.add_num - cpr.add_num == 0 \
        else 1 if mpr.add_num - cpr.add_num > 0 \
        else -1
    del_num1 = 0 if mpr.del_num - cpr.del_num == 0 \
        else 1 if mpr.del_num - cpr.del_num > 0 \
        else -1
    change_file_num1 = 0 if mpr.change_file_num - cpr.change_file_num == 0 \
        else 1 if mpr.change_file_num - cpr.change_file_num > 0 \
        else -1
    
    CPR1 = CPR(url1, merged1, time_span1, language1, dev_type1, comment_num1, review_comment_num1,commit_num1, add_num1
               , del_num1, change_file_num1)

    url2 = cpr.url
    merged2 = cpr.merged
    time_span2 = 0 if cpr.time_span - mpr.time_span == 0 else 1 if cpr.time_span - mpr.time_span > 0 else -1
    language2 = cpr.language
    dev_type2 = cpr.dev_type
    comment_num2 = 0 if cpr.comment_num - mpr.comment_num == 0 \
        else 1 if cpr.comment_num - mpr.comment_num > 0 \
        else -1
    review_comment_num2 = 0 if cpr.review_comment_num - mpr.review_comment_num == 0 \
        else 1 if cpr.review_comment_num - mpr.review_comment_num > 0 \
        else -1
    commit_num2 = 0 if cpr.commit_num - mpr.commit_num == 0 \
        else 1 if cpr.commit_num - mpr.commit_num > 0 \
        else -1
    add_num2 = 0 if cpr.add_num - mpr.add_num == 0 \
        else 1 if cpr.add_num - mpr.add_num > 0 \
        else -1
    del_num2 = 0 if cpr.del_num - mpr.del_num == 0 \
        else 1 if cpr.del_num - mpr.del_num > 0 \
        else -1
    change_file_num2 = 0 if cpr.change_file_num - mpr.change_file_num == 0 \
        else 1 if cpr.change_file_num - mpr.change_file_num > 0 \
        else -1

    CPR2 = CPR(url2, merged2, time_span2, language2, dev_type2, comment_num2, review_comment_num2, commit_num2, add_num2
               , del_num2, change_file_num2)

    return CPR1, CPR2


def cal_lift_sup_conf(lis_A, lis_O, attr_a):
    cnt_A = Counter(lis_A)
    cnt_O = Counter(lis_O)

    lis_A_O = list(zip(lis_A, lis_O))
    cnt_A_O = Counter(lis_A_O)

    P_A = cnt_A[attr_a] / len(lis_A)
    P_O = cnt_O['True'] / len(lis_O)
    P_A_O = cnt_A_O[(attr_a, 'True')] / len(lis_A_O)

    return float(P_A_O / (P_A * P_O)), float(P_A_O), float(P_A_O / P_A)


def analysis(CPRs):
    attr_num_CPR = len(CPRs[0].tolist())
    merged_loc = 1
    str_attr_locs = [3]
    num_attr_locs = [i for i in range(4, attr_num_CPR)]

    locs = []
    locs.extend(str_attr_locs)
    locs.extend(num_attr_locs)
    index2attr = {0: "url", 1: "merged", 2: "language", 3: "dev_type", 4: "more_time_span", 5: "more_comment_num",
                  6: "more_review_comment_num", 7: "more_commit_num", 8: "more_add_num", 9: "more_del_num",
                  10: "more_change_file_num"}
    
    lis = []
    for i in range(len(CPRs)):
        CPRs[i].toString()
        lis.append(CPRs[i].tolist())

    arr = np.array(lis).T
    row_merged = arr[merged_loc]

    for index in locs:
        row_attr = arr[index]
        val_set = set(arr[index])
        val_lis = sorted(list(val_set))
        lift_lis = []
        sup_lis = []
        conf_lis = []
        labels = ["Indicator \\ Type"]
        for val in val_lis:
            # print(index2attr.get(index), val)
            # print(row_attr)
            lift, sup, conf = cal_lift_sup_conf(row_attr, row_merged, val)
            lift_lis.append(lift)
            sup_lis.append(sup)
            conf_lis.append(conf)
            labels.append(val)

        print_results(index2attr.get(index), labels, lift_lis, sup_lis, conf_lis, val_lis)


def print_results(attr, labels, lift_lis, sup_lis, conf_lis, val_lis):
    format_labels = []
    for index, _ in enumerate(labels):
        format_labels.append("{0[%d]:^20}" % index)
    fstr = "|" + "|".join(format_labels) + "|"

    line_len = len(labels) * 20 + len(labels) + 1
    print("-" * line_len)
    print(("|{:^%d" % (line_len - 2) + "}|").format(attr + "-> Merged"))
    print("-" * line_len)
    print(fstr.format(labels))
    print("-" * line_len)
    for idc, idc_lis in list(zip(["Lift", "Sup", "Conf"], [lift_lis, sup_lis, conf_lis])):
        print_indicator(idc, fstr, val_lis, idc_lis)
    print("-" * line_len)


def print_indicator(idc, fstr, val_lis, idc_lis):
    val2idc = dict(zip(val_lis, idc_lis))
    st = [idc]

    for item in val2idc.items():
        st.append("%.3f" % (item[1]))
        # print(item)
    # print(idc + ":", ", ".join(st))
    print(fstr.format(st))
    

if __name__ == '__main__':
    merged_url_sets, url2merged_prs, url2closed_prs = read_excel()
    CPRs = getCPRs(merged_url_sets, url2merged_prs, url2closed_prs)
    analysis(CPRs)



