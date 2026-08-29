"""나만의 프롬프트 관리 프로그램 (콘솔 기반)"""

# 카테고리 정의
CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

# 기본 프롬프트 데이터 (이전 미션 결과물 3개 이상)
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 "
                   "SEO에 최적화된 블로그 글을 작성해주세요. 서론, 본론, 결론 "
                   "구조를 갖추고, 독자의 관심을 끄는 제목을 3개 제안해주세요.",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "제품 썸네일 생성",
        "content": "다음 제품의 매력적인 썸네일 이미지를 생성해주세요. "
                   "밝은 배경, 제품 중심 구도, 고급스러운 느낌을 강조합니다.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": "당신은 15년 경력의 IT 컨설턴트입니다. 기술 용어를 쉽게 "
                   "풀어 설명하며, 항상 실무 예시를 함께 제시합니다.",
        "category": "페르소나",
        "favorite": False
    },
]


def show_menu():
    """메인 메뉴를 출력한다."""
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


def input_nonempty(message):
    """비어있지 않은 값을 받을 때까지 반복 입력한다."""
    while True:
        value = input(message).strip()
        if value:
            return value
        print("⚠️ 값을 입력해주세요.")


def select_category():
    """카테고리를 선택하거나 직접 입력받는다."""
    print("\n카테고리 선택:")
    for i, cat in enumerate(CATEGORIES, start=1):
        print(f"{i}) {cat}")
    print(f"{len(CATEGORIES)+1}) 직접 입력")

    while True:
        choice = input("선택: ").strip()
        if choice.isdigit():
            num = int(choice)
            if 1 <= num <= len(CATEGORIES):
                return CATEGORIES[num - 1]
            if num == len(CATEGORIES) + 1:
                return input_nonempty("카테고리 직접 입력: ")
        print("⚠️ 올바른 번호를 입력하세요.")


def add_prompt():
    """새 프롬프트를 추가한다."""
    print("\n=== 프롬프트 추가 ===")
    title = input_nonempty("제목: ")
    content = input_nonempty("내용: ")
    category = select_category()
    prompts.append({
        "title": title, "content": content,
        "category": category, "favorite": False
    })
    print("\n프롬프트가 추가되었습니다!")


def format_line(index, p):
    """목록 한 줄을 포맷한다."""
    star = " ⭐" if p["favorite"] else ""
    return f"{index}. [{p['category']}] {p['title']}{star}"


def show_list():
    """전체 프롬프트 목록을 출력한다."""
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    for i, p in enumerate(prompts, start=1):
        print(format_line(i, p))
    print(f"\n총 {len(prompts)}개의 프롬프트")


def show_by_category():
    """카테고리별로 프롬프트를 조회한다."""
    print("\n=== 카테고리별 조회 ===")
    category = select_category()
    result = [p for p in prompts if p["category"] == category]
    if not result:
        print(f"\n[{category}] 카테고리에 프롬프트가 없습니다.")
        return
    print(f"\n[{category}] 카테고리 프롬프트:")
    for i, p in enumerate(result, start=1):
        print(format_line(i, p))
    print(f"\n총 {len(result)}개의 프롬프트")


def search_prompt():
    """키워드로 제목/내용을 검색한다."""
    print("\n=== 프롬프트 검색 ===")
    keyword = input_nonempty("검색어: ")
    result = [p for p in prompts
              if keyword in p["title"] or keyword in p["content"]]
    if not result:
        print("\n검색 결과가 없습니다.")
        return
    print("\n검색 결과:")
    for i, p in enumerate(result, start=1):
        print(format_line(i, p))
    print(f"\n{len(result)}개의 프롬프트를 찾았습니다.")


def show_detail():
    """번호로 프롬프트 상세 내용을 출력한다."""
    print("\n=== 프롬프트 상세 보기 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    num = input("번호 입력: ").strip()
    if not num.isdigit() or not (1 <= int(num) <= len(prompts)):
        print("⚠️ 올바른 번호가 아닙니다.")
        return
    p = prompts[int(num) - 1]
    star = "⭐" if p["favorite"] else "없음"
    print("\n" + "─" * 30)
    print(f"제목: {p['title']}")
    print(f"카테고리: {p['category']}")
    print(f"즐겨찾기: {star}")
    print("─" * 30)
    print("내용:")
    print(p["content"])
    print("─" * 30)


def manage_favorite():
    """즐겨찾기를 추가/해제한다."""
    print("\n=== 즐겨찾기 관리 ===")
    show_list()
    if not prompts:
        return
    num = input("\n프롬프트 번호 입력: ").strip()
    if not num.isdigit() or not (1 <= int(num) <= len(prompts)):
        print("⚠️ 올바른 번호가 아닙니다.")
        return
    p = prompts[int(num) - 1]
    p["favorite"] = not p["favorite"]
    state = "추가했습니다" if p["favorite"] else "해제했습니다"
    print(f"'{p['title']}' 프롬프트를 즐겨찾기에 {state}!")


def show_favorites():
    """즐겨찾기된 프롬프트만 출력한다."""
    print("\n=== 즐겨찾기 목록 ===")
    result = [p for p in prompts if p["favorite"]]
    if not result:
        print("즐겨찾기된 프롬프트가 없습니다.")
        return
    for i, p in enumerate(result, start=1):
        print(format_line(i, p))
    print(f"\n총 {len(result)}개의 즐겨찾기")


def main():
    """프로그램 메인 루프."""
    actions = {
        "1": add_prompt, "2": show_list, "3": show_by_category,
        "4": search_prompt, "5": show_detail,
        "6": manage_favorite, "7": show_favorites,
    }
    while True:
        show_menu()
        choice = input("선택: ").strip()
        if choice == "0":
            print("\n👋 프로그램을 종료합니다. 수고하셨습니다!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("⚠️ 잘못된 번호입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()