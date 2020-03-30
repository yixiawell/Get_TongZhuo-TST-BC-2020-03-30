import os, concurrent.futures
def merge(path,name):
    print(name)
    with open(os.path.join(path, "ts.m3u8"),"r+") as f:
        ts_list = f.readlines()
    ts_list = [os.path.join(path, i[i.rfind("-") + 1:].replace("\n", "")) for i in ts_list if i.find("#")]
    book = open(os.path.join(path,"{}.mp4".format(name)), "ab+")
    for t in ts_list:
        try:
            with open(t,"rb+") as f:
                b = f.read()
            book.write(b)
            os.remove(t)
        except:
            with open(os.path.join(path,"未写入.txt"),"a+") as f:
                f.write(t)
                f.write("\n")
    book.close()

if __name__ == '__main__':
    path = r".\视频"
    file_dirlist = os.listdir(path)
    path_list = [os.path.join(path, i) for i in file_dirlist]
    path_name_list = list(zip(file_dirlist,path_list))
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as process:
        fun1 = [process.submit(merge, p[1], p[0]) for p in path_name_list]
    print("已合并完成！！！")
