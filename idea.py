import random

def get_word_list():
    # 英検2級レベルの単語リスト（単語: 意味）
    return [
        ("increase", "増加する"),
        ("reduce", "減らす"),
        ("environment", "環境"),
        ("require", "必要とする"),
        ("improve", "改善する"),
        ("ability", "能力"),
        ("opportunity", "機会"),
        ("responsible", "責任がある"),
        ("community", "地域社会"),
        ("experience", "経験"),
        ("support", "支援する"),
        ("challenge", "挑戦"),
        ("protect", "守る"),
        ("develop", "発展させる"),
        ("prepare", "準備する"),
        ("provide", "提供する"),
        ("suggest", "提案する"),
        ("consider", "考慮する"),
        ("create", "創造する"),
        ("discover", "発見する"),
    ]

def ask_question(word, correct_meaning, all_meanings):
    choices = [correct_meaning]
    # 他の意味からランダムに2つ選ぶ
    wrong_choices = random.sample([m for m in all_meanings if m != correct_meaning], 2)
    choices.extend(wrong_choices)
    random.shuffle(choices)
    print(f"\n「{word}」の意味はどれ？")
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")
    answer = input("番号で答えてください: ")
    try:
        answer = int(answer)
        if choices[answer - 1] == correct_meaning:
            print("その調子！")
            return True
        else:
            print("おしいね")
            return False
    except:
        print("入力が正しくありません。おしいね")
        return False

def main():
    word_list = get_word_list()
    quiz = random.sample(word_list, 10)
    all_meanings = [meaning for _, meaning in word_list]
    correct_count = 0
    wrong_questions = []

    for word, meaning in quiz:
        result = ask_question(word, meaning, all_meanings)
        if result:
            correct_count += 1
        else:
            wrong_questions.append((word, meaning))

    print(f"\n正解率: {correct_count}/10 ({correct_count * 10}%)")

    if wrong_questions:
        print("\nアドバイス:")
        for word, meaning in wrong_questions:
            print(f"「{word}」は「{meaning}」です。例文を調べてみましょう！")
    else:
        print("全問正解！素晴らしいです！")

if __name__ == "__main__":
    main()