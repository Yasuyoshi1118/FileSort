import re, os, glob, shutil
# ファイル一覧を取得する --- (*1)

base_dir = os.path.dirname(__file__)

train = "train"
valid = "valid"
valid_dir = os.path.join(base_dir, valid)
train_dir = os.path.join(base_dir, train)

print("＋＋＋＋jpgファイルを処理開始＋＋＋＋")
# Cam1~Cam●まですべて実行する
for num in range(1,13):
    Cam_num = "Cam" + str(num)
    Cam_dir = Cam_num + "/" + "*.jpg"

    files = glob.glob(Cam_dir)
    print("処理中フォルダ",Cam_num)

    # 各ファイルごとに処理を行う --- (*2)
    for f in files:
    
        c = re.search(r'[k][.][j][p][g]$', f)
        if c is None:
        # 正規表現マッチ --- (*3)
            m = re.search(r'[1-7][.][j][p][g]$', f)


            if m is None:


                if not os.path.exists(valid_dir):
                  os.mkdir(valid_dir)
                # ファイル名を決定してコピー --- (*6)
                copy_file = base_dir + "/" + f
                newfile = os.path.join(valid_dir, copy_file)
                shutil.copy(copy_file, valid_dir)
                #print("validfile:", newfile)
            else:
                # 保存先フォルダ名を決める --- (*5)

                if not os.path.exists(train_dir):
                  os.mkdir(train_dir)
                # ファイル名を決定してコピー --- (*6)
                #print("train_dir",train_dir)
                #print("f:",f)
                copy_file = base_dir + "/" + f
                newfile = os.path.join(train_dir, copy_file)
                shutil.copy(copy_file, train_dir)
                #print("trainfile:", newfile)
                #print("コピー:", newfile)
            
print("＋＋＋＋ｊsonファイルを処理開始＋＋＋＋")

for num in range(1,13):
    Cam_num = "Cam" + str(num)
    Cam_dir = Cam_num + "/" + "*.json"
    files = glob.glob(Cam_dir)
    
    print("処理中フォルダ",Cam_num)

    # 各ファイルごとに処理を行う --- (*2)
    for f in files:
        m = re.search(r'[1-7][.][j][s][o][n]$', f)


        if m is None:


            if not os.path.exists(valid_dir):
              os.mkdir(valid_dir)
            # ファイル名を決定してコピー --- (*6)
            copy_file = base_dir + "/" + f
            newfile = os.path.join(valid_dir, copy_file)
            shutil.copy(copy_file, valid_dir)
            #print("validfile:", newfile)
        else:
            # 保存先フォルダ名を決める --- (*5)

            if not os.path.exists(train_dir):
              os.mkdir(train_dir)
            # ファイル名を決定してコピー --- (*6)
            #print("train_dir",train_dir)
            #print("f:",f)
            copy_file = base_dir + "/" + f
            newfile = os.path.join(train_dir, copy_file)
            shutil.copy(copy_file, train_dir)
            #print("trainfile:", newfile)
            #print("コピー:", newfile)
        