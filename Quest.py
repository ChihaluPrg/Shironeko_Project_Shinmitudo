from OpenCV2 import *

quest_13_3_path = "img/quest_13_3.jpg"
go_path = "img/go.jpg"
item_kouka_path = "img/item_kouka.jpg"
quest_rule_path = "img/ok_kakunin.jpg"
item_selection_path = "img/item_selection.jpg"
boost_item_path = "img/boost_2bai.jpg"
max_path = "img/max.jpg"
item_use_path = "img/item_use.jpg"
result_ok_path = "img/result_ok.jpg"
retry_path = "img/retry.jpg"
retry_yes_path = "img/retry_yes.jpg"
go_room_ok_path = "img/go_room_ok.jpg"
go_room_path = "img/go_room.jpg"

def process_quest():
    while True :
        position = find_template_position(quest_13_3_path)
        if position:
            tap_on_device(position[0], position[1])
            print("クエスト：飛来せし岩を破壊せよ！を選択しました")
            time.sleep(1)
            break
        else:
            print("クエスト：飛来せし岩を破壊せよ！を選択できませんでした...再試行します...")
    count = 0
    while True :
        position = find_template_position(go_path)
        if position:
            tap_on_device(position[0], position[1])
            count += 1
            print(f"\n{count}回目の処理を開始します")
            print("挑戦ボタンをタップしました")
            time.sleep(13)
            break
        else:
            print("挑戦ボタンをタップできませんでした...再試行します...")

    try:
        count2 = 1
        while True :
            while True:
                position = find_template_position(quest_rule_path)
                if position:
                    tap_on_device(position[0], position[1])
                    print("クリア条件をタップしました")
                    time.sleep(20)
                    break
                else:
                    print("クリア条件をタップできませんでした")
            while True:
                position = find_template_position(go_room_path)
                if position:
                    print("キャラの親密度が上がりました、キャラ変更をしてください")
                    while True:
                        position = find_template_position(go_room_ok_path)
                        if position:
                            tap_on_device(position[0], position[1])
                            print("OKボタンをタップしました")
                            time.sleep(2)
                            shinmitudo_up()
                            break
                        else:
                            print("OKボタンをタップできませんでした")
                    continue
                else:
                    break


            position = find_template_position(item_kouka_path)
            if position:
                print("アイテム効果は切れていません")
                time.sleep(2)
            else:
                print("アイテム効果が切れている為、アイテムを使用する処理を行います")
                time.sleep(3)
                while True:
                    position = find_template_position(result_ok_path)
                    if position:
                        tap_on_device(position[0], position[1])
                        print("OKボタンをタップしました")
                        time.sleep(7)
                        item_use()
                        count2 += 1
                        break
                    else:
                        print("OKボタンをタップできませんでした")
                continue

            while True:
                position = find_template_position(retry_path)
                if position:
                    tap_on_device(position[0], position[1])
                    time.sleep(1.5)
                    print("再挑戦ボタンをタップしました")
                    break
                else:
                    print("再挑戦ボタンをタップできませんでした...再試行します...")

            while True:
                position = find_template_position(retry_yes_path)
                if position:
                    tap_on_device(position[0], position[1])
                    print("はいボタンをタップしました")
                    count2 += 1
                    print(f"\n{count2}回目の処理を開始します")
                    time.sleep(15)
                    break
                else:
                    print("はいボタンをタップできませんでした")
    except KeyboardInterrupt:
        print("ループを終了しました")


def item_use():
    while True :
        position = find_template_position(quest_13_3_path)
        if position:
            tap_on_device(position[0], position[1])
            print("クエスト：飛来せし岩を破壊せよ！を選択しました")
            time.sleep(2)
            break
        else:
            print("クエスト：飛来せし岩を破壊せよ！を選択できませんでした...再試行します...")

    while True :
        position = find_template_position(item_selection_path)
        if position:
            tap_on_device(position[0], position[1])
            print("アイテム選択をタップしました")
            break
        else:
            print("アイテム選択をタップできませんでした")

    while True :
        position = find_template_position(boost_item_path)
        if position:
            tap_on_device(position[0], position[1])
            print("冒険入門書～親密度～を選択しました")
            break
        else:
            print("アイテムを選択できませんでした...再試行します...")

    while True :
        position = find_template_position(go_path)
        if position:
            tap_on_device(position[0], position[1])
            print("挑戦ボタンをタップしました")
            while True:
                position = find_template_position(item_use_path)
                if position:
                    tap_on_device(position[0], position[1])
                    print("冒険入門書～親密度～を使用しました")
                    break
                else:
                    print("アイテムを使用できませんでした...再試行します...")
            time.sleep(13)
            break
        else:
            print("挑戦ボタンをタップできませんでした...再試行します...")

    while True:
        position = find_template_position(quest_rule_path)
        if position:
            tap_on_device(position[0], position[1])
            print("クリア条件をタップしました")
            time.sleep(20)
            break
        else:
            print("クリア条件をタップできませんでした")

def shinmitudo_up():

    while True:
        position = find_template_position(result_ok_path)
        if position:
            tap_on_device(position[0], position[1])
            time.sleep(3)
            break
        else:
            print("OKボタンをタップできませんでした")
    while True:
        position = find_template_position(quest_13_3_path)
        if position:
            time.sleep(3)
            tap_on_device(position[0], position[1])
            print("クエスト：飛来せし岩を破壊せよ！を選択しました")
            time.sleep(2)
            break
        else:
            print("クエスト：飛来せし岩を破壊せよ！を選択できませんでした...再試行します...")
    while True:
        user_input = input("キャラ変更が終わったら（y）を押してください: ")
        if user_input.lower() == 'y':
            break
        else:
            print("無効な入力です")
    while True :
        position = find_template_position(go_path)
        if position:
            tap_on_device(position[0], position[1])
            print("挑戦ボタンをタップしました")
            break
        else:
            print("挑戦ボタンをタップできませんでした...再試行します...")

    while True:
        position = find_template_position(quest_rule_path)
        if position:
            tap_on_device(position[0], position[1])
            print("クリア条件をタップしました")
            time.sleep(20)
            break
        else:
            print("クリア条件をタップできませんでした")
