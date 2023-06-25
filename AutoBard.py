from bardapi import Bard

def ask_bard(question):
    token = 'XXXXXXXXXXXX'  # あなたの__Secure-1PSID値 
    bard = Bard(token=token)
    step = bard.get_answer("内容からタスクを3ステップに分けて下さい" + question)['content']
    task1 = bard.get_answer("タスクのステップ1を実行してください" + step)['content']
    task2 = bard.get_answer("タスクのステップ2を実行してください" + step)['content']
    task3 = bard.get_answer("タスクのステップ3を実行してください" + step)['content']
    output = bard.get_answer("内容を総評して詳しく詳細なアウトプットを出力して下さい" + task1 + task2 + task3 )['content']
    return output  # ここを修正しました

# 外部からの入力を受け取る
question = input("タスクを教えて下さい：")
output = ask_bard(question)  
print("アウトプット:" + output)
