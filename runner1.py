import random

def generate_athlete_data(num_athletes):
    names = [
        "佐藤 美咲", "鈴木 彩花", "高橋 由紀", "田中 美穂", "伊藤 さくら",
        "渡辺 亜美", "山本 真由", "中村 愛", "小林 優子", "加藤 里奈",
        "吉田 美和", "山田 友香", "佐々木 佳奈", "斎藤 美紀", "松本 由美",
        "井上 さやか", "木村 朋美", "林 由佳", "清水 麻衣", "山口 由紀"
    ]

    prefectures = [
        "北海道", "青森県", "岩手県", "宮城県", "秋田県", "山形県", "福島県",
        "茨城県", "栃木県", "群馬県", "埼玉県", "千葉県", "東京都", "神奈川県",
        "新潟県", "富山県", "石川県", "福井県", "山梨県", "長野県", "岐阜県",
        "静岡県", "愛知県", "三重県", "滋賀県", "京都府", "大阪府", "兵庫県",
        "奈良県", "和歌山県", "鳥取県", "島根県", "岡山県", "広島県", "山口県",
        "徳島県", "香川県", "愛媛県", "高知県", "福岡県", "佐賀県", "長崎県",
        "熊本県", "大分県", "宮崎県", "鹿児島県", "沖縄県"
    ]

    athletes = []

    for i in range(num_athletes):
        name = names[i % len(names)]
        age = random.randint(10, 70)
        time = round(random.uniform(9.56, 12.99), 2)
        prefecture = random.choice(prefectures)
        athletes.append((name, age, time, prefecture))

    # タイムが良い順にソート
    athletes.sort(key=lambda x: x[2])

    return athletes

def main():
    num_athletes = 20
    athlete_data = generate_athlete_data(num_athletes)

    print("選手データ（名前, 年齢, タイム, 出身都道府県）:")
    for athlete in athlete_data:
        print(athlete)

if __name__ == "__main__":
    main()