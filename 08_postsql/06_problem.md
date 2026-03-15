# 실전 문제 1: 영화 언어 조회 (JOIN)

**배경 (Scenario)**
고객들에게 영화의 기본 언어 정보를 함께 제공하려고 합니다. 영화 제목과 해당 영화의 언어 이름을 확인해주세요.

**요구사항 (Requirements)**
1. **대상 선별**: `film`, `language` 테이블을 활용하세요.
2. **최종 결과물**:
   - `title`: 영화 제목
   - `name`: 언어 이름
3. **정렬**: 영화 제목(`title`)을 기준으로 오름차순 정렬하세요.

---

**💡 관련 테이블 (Tables)**
- `film`: 영화 정보 (`language_id` 컬럼 포함)
- `language`: 데이터베이스 내 언어 정보

<br>

---

| title | name |
| :--- | :--- |
| Academy Dinosaur | English              |
| Ace Goldfinger | English              |
| Adaptation Holes | English              |
| Affair Prejudice | English              |
| African Egg | English              |
| Agent Truman | English              |
| Airplane Sierra | English              |
| Airport Pollock | English              |
| Alabama Devil | English              |
| Aladdin Calendar | English              |



# 실전 문제 2: 고객 주소 정보 조회 (JOIN)

**배경 (Scenario)**
배송 안내를 위해 고객의 상세 주소 정보가 필요합니다. 고객의 이름과 이메일, 그리고 등록된 주소를 추출해주세요.

**요구사항 (Requirements)**
1. **대상 선별**: `customer`, `address` 테이블을 활용하세요.
2. **최종 결과물**:
   - `first_name`: 고객 이름
   - `last_name`: 고객 성
   - `email`: 이메일
   - `address`: 주소
3. **정렬**: 고객의 이름(`first_name`)을 기준으로 오름차순 정렬하세요.

---

**💡 관련 테이블 (Tables)**
- `customer`: 고객 정보 (`address_id` 컬럼 포함)
- `address`: 주소 정보

<br>

---

| first\_name | last\_name | email | address |
| :--- | :--- | :--- | :--- |
| Aaron | Selby | aaron.selby@sakilacustomer.org | 1519 Santiago de los Caballeros Loop |
| Adam | Gooch | adam.gooch@sakilacustomer.org | 230 Urawa Drive |
| Adrian | Clary | adrian.clary@sakilacustomer.org | 1986 Sivas Place |
| Agnes | Bishop | agnes.bishop@sakilacustomer.org | 866 Shivapuri Manor |
| Alan | Kahn | alan.kahn@sakilacustomer.org | 753 Ilorin Avenue |
| Albert | Crouse | albert.crouse@sakilacustomer.org | 1641 Changhwa Place |
| Alberto | Henning | alberto.henning@sakilacustomer.org | 502 Mandi Bahauddin Parkway |
| Alex | Gresham | alex.gresham@sakilacustomer.org | 251 Florencia Drive |
| Alexander | Fennell | alexander.fennell@sakilacustomer.org | 231 Kaliningrad Place |
| Alfred | Casillas | alfred.casillas@sakilacustomer.org | 1727 Matamoros Place |




# 실전 문제 3: 도시 및 국가 정보 조회 (JOIN)

**배경 (Scenario)**
각 도시에 대해 어느 국가에 속해 있는지 알아보기 위해 도시 이름과 해당 국가 이름을 함께 나열해주세요.

**요구사항 (Requirements)**
1. **대상 선별**: `city`, `country` 테이블을 활용하세요.
2. **최종 결과물**:
   - `city`: 도시 이름
   - `country`: 국가 이름
3. **정렬**: 국가 이름(`country`) 오름차순, 동일한 국가일 경우 도시 이름(`city`) 오름차순 정렬하세요.

---

**💡 관련 테이블 (Tables)**
- `city`: 도시 정보 (`country_id` 컬럼 포함)
- `country`: 국가 정보 

<br>

---

| city | country |
| :--- | :--- |
| Kabul | Afghanistan |
| Batna | Algeria |
| Bchar | Algeria |
| Skikda | Algeria |
| Tafuna | American Samoa |
| Benguela | Angola |
| Namibe | Angola |
| South Hill | Anguilla |
| Almirante Brown | Argentina |
| Avellaneda | Argentina |


# 실전 문제 4: 활성 고객 한정 우수 직원 평가 (GROUP BY, JOIN)

**배경 (Scenario)**
인사팀(HR)에서 결제 처리 건수가 많고 금액이 높은 우수 직원을 포상하고자 합니다. 단, 회사의 방침상 현재 활성 상태인 고객(Active Customer)이 결제한 금액만 직원의 실적으로 인정하기로 했습니다. (비활성 고객의 결제건은 제외)

**요구사항 (Requirements)**
1. **대상 선별**: `staff`, `payment`, `customer` 테이블을 활용하세요.
2. **조건 필터링**: 결제를 진행한 고객의 계정 상태가 활성(`active = 1` 또는 `activebool = true` - PostgreSQL버전에 따라 다를 수 있음, 일반적으로 active의 자료형이 integer라면 1)인 경우만 대상으로 합니다. 주의할 점은 직원의 활성 상태가 아니라 결제한 **고객의 활성 상태**라는 점입니다!
3. **실적 집계**: 직원별로 처리한 총 결제 금액(`amount` 합계)을 계산하세요. 
4. **결과 필터링**: 총 결제 금액이 **20,000 이상**인 직원만 결과에 포함하세요.
5. **최종 결과물**:
   - `staff_id`: 직원 ID
   - `first_name`: 직원 이름
   - `last_name`: 직원 성
   - `total_active_customer_payment`: 활성 고객 대상 총 결제 처리 금액
6. **정렬**: 총 결제 금액을 기준으로 내림차순 정렬하세요.

---

**💡 관련 테이블 (Tables)**
- `staff`: 직원 정보
- `payment`: 결제 내역
- `customer`: 고객 정보 (`active` 컬럼 포함)

<br>

---
**정답**

| staff\_id | first\_name | last\_name | total\_active\_customer\_payment |
| :--- | :--- | :--- | :--- |
| 2 | Jon | Stephens | 30260.89 |
| 1 | Mike | Hillyer | 29540.84 |``
---


# 실전 문제 5: 첫 대여 기념일 이메일 발송 타겟 추출 (PARTITION BY, JOIN)

**배경 (Scenario)**
고객 서비스(CS) 팀에서 당사 서비스를 처음 이용했던 순간을 기념하기 위해, 모든 고객에게 "당신의 첫 대여 영화는 OOO 였습니다!"라는 내용의 감사 이메일을 보내려고 합니다. 

**요구사항 (Requirements)**
1. **첫 대여 기록 색출**: 각 고객이 **가장 처음으로(가장 이른 날짜에)** 대여한 `rental` 기록을 찾아야 합니다.
2. **영화 제목 연결**: 해당 첫 대여 기록이 어떤 영화였는지 알아내기 위해 `inventory`, `film` 테이블을 조인하세요.
3. **최종 결과물**:
   - `customer_id`: 고객 ID
   - `customer_name`: 고객 전체 이름 (이름과 성을 공백으로 연결, 예: 'MARY SMITH')
   - `first_rental_date`: 첫 대여 일자
   - `first_rented_film_title`: 처음 대여한 영화 제목
4. **정렬**: 고객 ID를 기준으로 오름차순 정렬하세요.

---

**💡 관련 테이블 (Tables)**
- `customer`: 고객 정보
- `rental`: 대여 내역
- `inventory`: 재고 정보
- `film`: 영화 정보

**💡 구현 힌트**
- 단순히 고객별 최솟값(`MIN(rental_date)`)을 구하는 `GROUP BY`만 사용하면, 그 날짜에 빌린 "영화 제목"을 같은 레벨에서 SELECT 하기 매우 까다롭습니다. 
- 윈도우 함수 `ROW_NUMBER()`에 `PARTITION BY`를 활용해 고객별 대여 일자 순으로 순위를 매기고, 1순위인 데이터만 외곽 쿼리(Inline view 또는 CTE 활용)에서 필터링해 보세요.

<br>

---

**정답**

| customer\_id | customer\_name | first\_rental\_date | first\_rented\_film\_title |
| :--- | :--- | :--- | :--- |
| 1 | Mary Smith | 2005-05-25 11:30:37.000000 | Patient Sister |
| 2 | Patricia Johnson | 2005-05-27 00:09:24.000000 | Doors President |
| 3 | Linda Williams | 2005-05-27 17:17:09.000000 | Rings Heartbreakers |
| 4 | Barbara Jones | 2005-06-15 09:31:28.000000 | Dogma Family |
| 5 | Elizabeth Brown | 2005-05-29 07:25:16.000000 | Tootsie Pilot |
| 6 | Jennifer Davis | 2005-05-25 08:43:32.000000 | Submarine Bed |
| 7 | Maria Miller | 2005-05-25 06:04:08.000000 | Ridgemont Submarine |
| 8 | Susan Wilson | 2005-05-30 03:43:54.000000 | Northwest Polish |
| 9 | Margaret Moore | 2005-05-27 05:01:28.000000 | Mulan Moon |
| 10 | Dorothy Taylor | 2005-05-31 19:36:30.000000 | Snowman Rollercoaster |

---



# 실전 문제 6: 특정 등급 영화의 대여 건수와 인기도 통계 (LEFT JOIN, GROUP BY, CASE)

**배경 (Scenario)**
재고 관리 팀에서 영화 등급별 수요를 파악하고 있습니다. 이번에는 'PG-13' 또는 'R' 등급을 받은 영화들만을 대상으로, 각 영화가 누적으로 몇 번이나 대여되었는지 확인하고 인기도(상태)를 라벨로 붙여 보고서를 작성하고자 합니다.

**요구사항 (Requirements)**
1. **대상 선별**: `film` 테이블에서 영화 등급(`rating` 텍스트 값 적용)이 'PG-13' 이거나 'R'인 영화만 추출하세요. (문자열 대소문자 혹시 구분이 필요하다면 정확히 기입하세요.)
2. **대여 횟수 집계**: 해당 영화들이 지금까지 총 몇 번 대여되었는지 계산하세요. 
   - **(주의)** 대여된 적이 단 한 번도 없는 영화(0회)도 리포트 누락 방지를 위해 결과에 반드시 포함되어야 합니다!
3. **인기도 라벨링**: 총 대여 횟수를 기준으로 다음 조건에 맞춰 `popularity_label`을 부여하세요.
   - 대여 횟수가 20회 초과(> 20): `'Hot'`
   - 대여 횟수가 20회 이하(<= 20, 0회 포함): `'Normal'`
4. **최종 결과물**:
   - `film_id`: 영화 ID
   - `title`: 영화 제목
   - `rating`: 영화 등급
   - `total_rentals`: 총 대여 횟수
   - `popularity_label`: 인기도 라벨
5. **정렬**: 총 대여 횟수 내림차순 정렬하고, 횟수가 같다면 영화 ID 오름차순으로 정렬하세요.

---

**💡 관련 테이블 (Tables)**
- `film`: 영화 정보 (`rating` 컬럼 포함)
- `inventory`: 재고 정보
- `rental`: 대여 내역

**💡 구현 힌트**
- 대여 이력이 없는 영화를 포함하려면 부모 테이블(`film`)을 기준으로 `LEFT JOIN`을 연쇄적으로 수행해야 합니다.
- 단순히 `COUNT(*)`를 사용하면 조인 실패로 생긴 NULL 행들도 1건으로 카운팅하는 우를 범할 수 있습니다. `rental_id`처럼 교집합 시에만 존재하는 데이터를 `COUNT(컬럼명)` 안에 넣어 정확하게 집계되도록 하세요.

<br>

---

**정답**

| film\_id | title | rating | total\_rentals | popularity\_label |
| :--- | :--- | :--- | :--- | :--- |
| 738 | Rocketeer Mother | PG-13 | 33 | Hot |
| 489 | Juggler Hardly | PG-13 | 32 | Hot |
| 730 | Ridgemont Submarine | PG-13 | 32 | Hot |
| 418 | Hobbit Alien | PG-13 | 31 | Hot |
| 621 | Network Peak | PG-13 | 31 | Hot |
| 735 | Robbers Joon | PG-13 | 31 | Hot |
| 285 | English Bulworth | PG-13 | 30 | Hot |
| 403 | Harry Idaho | PG-13 | 30 | Hot |
| 563 | Massacre Usual | R | 30 | Hot |
| 748 | Rugrats Shakespeare | PG-13 | 30 | Hot |
