import global_var
import csv
import os
import time

def write(filename, cjk_char_count, unicode_char_count, lang):
    #language localization
    if lang == "zhs": #simplified chinese
        cjk_jian_namelist = global_var.cjk_jian_list_zhs
        cjk_jian_fan_namelist = global_var.cjk_jian_fan_list_zhs
        cjk_fan_namelist = global_var.cjk_fan_list_zhs
        unicode_namelist = global_var.unicode_list_zhs
        titles = global_var.titles_zhs
        csv_title = "#名称,计数,总数"
    elif lang == "zht": #traditional chinese
        cjk_jian_namelist = global_var.cjk_jian_list_zht
        cjk_jian_fan_namelist = global_var.cjk_jian_fan_list_zht
        cjk_fan_namelist = global_var.cjk_fan_list_zht
        unicode_namelist = global_var.unicode_list_zht
        titles = global_var.titles_zht
        csv_title = "#名稱,計數,總數"
    else:
        cjk_jian_namelist = global_var.cjk_jian_list_en
        cjk_jian_fan_namelist = global_var.cjk_jian_fan_list_en
        cjk_fan_namelist = global_var.cjk_fan_list_en
        unicode_namelist = global_var.unicode_list
        titles = global_var.titles_en
        csv_title = "#name,count,full_size"
    
    # create folder
    if not os.path.isdir(os.path.join(global_var.main_directory, "cjk_report")):
        os.mkdir(os.path.join(global_var.main_directory, "cjk_report"))
    # prepare filename
    output_filename = time.strftime("%Y%m%d_%H%M%S") + "_" + filename + ".txt"
    output_fullpath = uniquify(os.path.join(global_var.main_directory, "cjk_report", output_filename))
    output_file = open(output_fullpath, "w", encoding="utf-8", newline='') #newline "" for DictWriter to automatic insert \r\n
    output_writer = csv.DictWriter(output_file, ("name", "count", "full_size"), quoting=csv.QUOTE_NONNUMERIC)


    # start writing
    if lang == "zht":
        write_list(output_file, output_writer, titles["trad"], csv_title, cjk_fan_namelist, cjk_char_count, global_var.cjk_count)
    else:
        write_list(output_file, output_writer, titles["simp"], csv_title, cjk_jian_namelist, cjk_char_count, global_var.cjk_count)
    
    output_file.write("===\n\n")

    write_list(output_file, output_writer, titles["simptrad"], csv_title, cjk_jian_fan_namelist, cjk_char_count, global_var.cjk_count)

    output_file.write("===\n\n")

    if lang == "zht":
        write_list(output_file, output_writer, titles["simp"], csv_title, cjk_jian_namelist, cjk_char_count, global_var.cjk_count)
    else:
        write_list(output_file, output_writer, titles["trad"], csv_title, cjk_fan_namelist, cjk_char_count, global_var.cjk_count)

    output_file.write("===\n\n")

    write_list(output_file, output_writer, titles["uni"], csv_title, unicode_namelist, unicode_char_count, global_var.unicode_count)

    output_file.write("===")

    output_file.close()

def write_list(output_file, output_writer, title, csv_title, name_list, count_arr, total_arr):
    output_file.write(f"=== %s ===\n" % (title))
    write_dict = []
    for varname, fullname in name_list.items():
        write_dict.append({"name":fullname, 
                                "count":count_arr[varname],
                                "full_size":total_arr[varname]})
    output_file.write(csv_title + "\n")
    output_writer.writerows(write_dict)

def uniquify(path):
    filename, extension = os.path.splitext(path)
    counter = 1

    while os.path.exists(path):
        path = filename + "#" + str(counter) + extension
        counter += 1

    return path