# ======================================================
# 나만의 프롬프트 관리 프로그램
# Python 3.10+ / 표준 라이브러리만 사용
# ======================================================

# ------------------------------------------------------
# 기본 데이터 (이전 미션에서 작성한 프롬프트 3개 이상)
# 리스트 + 딕셔너리 구조로 저장
# ------------------------------------------------------
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 "
                   "최적화된 블로그 글을 작성해주세요. 서론, 본론, 결론 구조를 갖추고, "
                   "독자의 관심을 끄는 제목을 3개 제안해주세요.",
        "category": "텍스트 생성",
        "favorite": True,
    },
    {
        "title": "제품 썸네일 생성",
        "content": "다음 제품의 매력적인 썸네일 이미지를 생성해주세요. 밝은 배경, "
                   "제품이 중앙에 오도록 구도를 잡아주세요.",
        "category": "이미지 생성",
        "favorite": False,
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": "당신은 20년 경력의 IT 컨설턴트입니다. 기술 용어를 쉽게 풀어 "
                   "설명하고, 실무 관점에서 조언해주세요.",
        "category": "페르소나",
        "favorite": False,
    },
    {
        "title": "뉴스 요약 프롬프트",
        "content": "다음 뉴스 기사를 3줄로 요약해주세요. 핵심 사실만 담고 "
                   "주관적인 해석은 배제해주세요.",
        "category": "자동화",
        "favorite": False,
    },
    {
        "title": "광고 스크립트 작성",
        "content": "30초 분량의 제품 광고 영상 스크립트를 작성해주세요. "
                   "후킹 멘트로 시작하고 행동 유도 문구로 마무리해주세요.",
        "category": "영상 생성",
        "favorite": False,
    },
]

# 미리 정의된 카테고리 목록
CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]


# ------------------------------------------------------
# 메뉴 출력
# ------------------------------------------------------
def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("8. 프롬프트 수정")
    print("0. 종료")


# ------------------------------------------------------
# 1. 프롬프트 추가
# ------------------------------------------------------
def add_prompt():
    print("\n=== 프롬프트 추가 ===")

    # 제목: 비어있으면 다시 입력
    while True:
        title = input("제목: ").strip()
        if title:
            break
        print("제목은 비워둘 수 없습니다. 다시 입력하세요.")

    # 내용: 비어있으면 다시 입력
    while True:
        content = input("내용: ").strip()
        if content:
            break
        print("내용은 비워둘 수 없습니다. 다시 입력하세요.")

    # 카테고리: 목록에서 선택하거나 직접 입력
    print("\n카테고리 선택:")
    for i, c in enumerate(CATEGORIES, start=1):
        print(f"{i}) {c}")
    choice = input("선택 (번호 또는 직접 입력): ").strip()

    if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
        category = CATEGORIES[int(choice) - 1]
    elif choice:
        category = choice
    else:
        category = "기타"

    # 리스트에 딕셔너리로 추가 (즐겨찾기 기본값 False)
    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
    })
    print("\n프롬프트가 추가되었습니다!")


# ------------------------------------------------------
# 즐겨찾기 표시용 별 문자 반환 (도우미 함수)
# ------------------------------------------------------
def star(prompt):
    return " ⭐" if prompt["favorite"] else ""


# ------------------------------------------------------
# 2. 프롬프트 목록
# ------------------------------------------------------
def show_list():
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    for i, p in enumerate(prompts, start=1):
        print(f"{i}. [{p['category']}] {p['title']}{star(p)}")
    print(f"\n총 {len(prompts)}개의 프롬프트")


# ------------------------------------------------------
# 3. 카테고리별 조회
# ------------------------------------------------------
def show_by_category():
    print("\n=== 카테고리별 조회 ===")
    for i, c in enumerate(CATEGORIES, start=1):
        print(f"{i}) {c}")
    choice = input("선택: ").strip()

    if not (choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES)):
        print("잘못된 선택입니다.")
        return

    category = CATEGORIES[int(choice) - 1]
    matched = [p for p in prompts if p["category"] == category]

    if not matched:
        print(f"\n[{category}] 카테고리에 프롬프트가 없습니다.")
        return

    print(f"\n[{category}] 카테고리 프롬프트:")
    for i, p in enumerate(matched, start=1):
        print(f"{i}. {p['title']}{star(p)}")
    print(f"\n총 {len(matched)}개의 프롬프트")


# ------------------------------------------------------
# 4. 프롬프트 검색 (제목 또는 내용)
# ------------------------------------------------------
def search_prompt():
    print("\n=== 프롬프트 검색 ===")
    keyword = input("검색어: ").strip()
    if not keyword:
        print("검색어를 입력하세요.")
        return

    matched = [
        p for p in prompts
        if keyword.lower() in p["title"].lower()
        or keyword.lower() in p["content"].lower()
    ]

    print("\n검색 결과:")
    if not matched:
        print("검색 결과가 없습니다.")
        return

    for i, p in enumerate(matched, start=1):
        print(f"{i}. [{p['category']}] {p['title']}{star(p)}")
    print(f"\n{len(matched)}개의 프롬프트를 찾았습니다.")


# ------------------------------------------------------
# 5. 프롬프트 상세 보기
# ------------------------------------------------------
def show_detail():
    print("\n=== 프롬프트 상세 보기 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    num = input("번호 입력: ").strip()
    if not (num.isdigit() and 1 <= int(num) <= len(prompts)):
        print("잘못된 번호입니다.")
        return

    p = prompts[int(num) - 1]
    print("\n" + "─" * 40)
    print(f"제목: {p['title']}")
    print(f"카테고리: {p['category']}")
    print(f"즐겨찾기: {'⭐' if p['favorite'] else '없음'}")
    print("─" * 40)
    print("내용:")
    print(p["content"])
    print("─" * 40)


# ------------------------------------------------------
# 6. 즐겨찾기 관리 (추가/해제 토글)
# ------------------------------------------------------
def manage_favorite():
    print("\n=== 즐겨찾기 관리 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    num = input("프롬프트 번호 입력: ").strip()
    if not (num.isdigit() and 1 <= int(num) <= len(prompts)):
        print("잘못된 번호입니다.")
        return

    p = prompts[int(num) - 1]
    p["favorite"] = not p["favorite"]

    if p["favorite"]:
        print(f"'{p['title']}' 프롬프트를 즐겨찾기에 추가했습니다!")
    else:
        print(f"'{p['title']}' 프롬프트를 즐겨찾기에서 해제했습니다!")


# ------------------------------------------------------
# 7. 즐겨찾기 목록
# ------------------------------------------------------
def show_favorites():
    print("\n=== 즐겨찾기 목록 ===")
    matched = [p for p in prompts if p["favorite"]]

    if not matched:
        print("즐겨찾기한 프롬프트가 없습니다.")
        return

    for i, p in enumerate(matched, start=1):
        print(f"{i}. [{p['category']}] {p['title']} ⭐")
    print(f"\n총 {len(matched)}개의 즐겨찾기")


# ------------------------------------------------------
# 8. 프롬프트 수정 (Enter 입력 시 기존 값 유지)
# ------------------------------------------------------
def edit_prompt():
    print("\n=== 프롬프트 수정 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list()
    num = input("\n수정할 번호 입력: ").strip()
    if not (num.isdigit() and 1 <= int(num) <= len(prompts)):
        print("잘못된 번호입니다.")
        return

    p = prompts[int(num) - 1]
    print("\n(변경하지 않을 항목은 그냥 Enter를 누르세요)")

    new_title = input(f"제목 [{p['title']}]: ").strip()
    if new_title:
        p["title"] = new_title

    new_content = input("내용 (기존 내용 유지는 Enter): ").strip()
    if new_content:
        p["content"] = new_content

    print("\n카테고리 선택:")
    for i, c in enumerate(CATEGORIES, start=1):
        print(f"{i}) {c}")
    choice = input(f"선택 [{p['category']}]: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
        p["category"] = CATEGORIES[int(choice) - 1]
    elif choice:
        p["category"] = choice

    print(f"\n'{p['title']}' 프롬프트가 수정되었습니다!")

# ------------------------------------------------------
# 메인 루프
# ------------------------------------------------------
def main():
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            manage_favorite()
        elif choice == "7":
            show_favorites() 
        elif choice == "8":
            edit_prompt()   
        elif choice == "0":
            print("\n프로그램을 종료합니다. 안녕히 가세요!")
            break
        else:
            print("\n잘못된 번호입니다. 다시 선택하세요.")


if __name__ == "__main__":
    main()