# ĐỒ ÁN: BÀI TOÁN DU LỊCH (TSP) VÀ PHÂN TÍCH GIẢI THUẬT

## 1. Giới thiệu dự án

**Bài toán:** Cho bản đồ du lịch, chọn tuyến đường đi qua nhiều điểm nổi tiếng với chi phí nhỏ nhất.

Dự án mô hình hóa đề bài thành bài toán **chọn tập điểm và thứ tự đi trong một ngân sách** (biến thể của TSP, còn gọi là Orienteering Problem), rồi nghiên cứu, cài đặt, kiểm thử và so sánh hiệu năng của ba chiến lược giải thuật:

- **Stage 1 – Greedy (Tham lam):** Từ địa điểm hiện tại, chọn địa điểm chưa thăm có tỉ lệ độ nổi tiếng / chi phí cao nhất mà vẫn còn nằm trong ngân sách.
- **Stage 2 – Brute Force / Backtracking (Vét cạn / Quay lui):** Duyệt các tuyến đường có thể bằng đệ quy quay lui, kết hợp nhánh cận để giảm số trường hợp cần xét.
- **Stage 3 – Divide & Conquer (Chia để trị):** Chia tập địa điểm thành các cụm nhỏ, chọn điểm và giải quyết từng cụm, rồi kết hợp thành một tuyến hoàn chỉnh.

Mục tiêu của dự án:

1. Hiểu và cài đặt ba chiến lược giải thuật bằng Python.
2. Thống nhất cấu trúc dữ liệu và giao diện giữa các module.
3. Kiểm tra tính hợp lệ của tuyến đường (đúng ngân sách) và độ chính xác của kết quả.
4. Đo thời gian thực thi và so sánh hiệu năng trên các bộ dữ liệu có kích thước khác nhau.
5. Đánh giá ưu điểm, hạn chế và tính phù hợp của từng phương pháp.
6. Thực hành làm việc nhóm, quản lý mã nguồn bằng Git/GitHub và viết báo cáo kỹ thuật.

**Lưu ý về tính tối ưu:** Greedy và phương pháp chia để trị do nhóm xây dựng không mặc nhiên tìm được nghiệm tối ưu toàn cục. Stage 2 được sử dụng làm nghiệm tham chiếu trên các bộ dữ liệu đủ nhỏ. Khi không thể chạy Stage 2 với dữ liệu lớn, báo cáo phải ghi rõ giới hạn so sánh, không được mặc nhiên xem kết quả của thuật toán khác là tối ưu.

---

## 2. Mô hình bài toán

Đề bài có hai vế mâu thuẫn nhau: "đi qua **nhiều điểm nổi tiếng**" (muốn đi nhiều) và "**chi phí nhỏ nhất**" (muốn đi ít). Dự án cân bằng hai vế bằng một ngân sách và độ nổi tiếng của từng điểm.

### 2.1. Dữ liệu của bài toán

- `N` địa điểm, đánh số `0` đến `N - 1`. Địa điểm `0` là điểm xuất phát và điểm kết thúc của tuyến.
- `cost[i][j]`: chi phí di chuyển trực tiếp từ điểm `i` đến điểm `j` (VNĐ).
- `fame[i]`: độ nổi tiếng của điểm `i` (số nguyên không âm, đề xuất thang từ 1 đến 10). Riêng điểm xuất phát có `fame[0] = 0` vì luôn được thăm.
- `budget`: ngân sách tối đa của cả chuyến đi (VNĐ).

### 2.2. Ràng buộc

- Tuyến đi bắt đầu tại `0` và quay về `0` (khép kín).
- Mỗi địa điểm được chọn chỉ thăm **đúng một lần**; không bắt buộc phải thăm tất cả địa điểm.
- Tổng chi phí của tuyến (tính cả chặng quay về `0`) **không được vượt quá `budget`**.

### 2.3. Mục tiêu tối ưu (so sánh theo thứ tự ưu tiên)

1. **Tối đa tổng độ nổi tiếng** `total_fame` của các điểm được thăm.
2. Nếu bằng nhau về `total_fame`, chọn tuyến có **tổng chi phí `total_cost` nhỏ nhất**.

Quy tắc so sánh này áp dụng thống nhất cho cả ba thuật toán và cho benchmark.

### 2.4. Cấu trúc dữ liệu bắt buộc: Ma trận chi phí 2 chiều

Dự án **bắt buộc** biểu diễn bản đồ bằng **ma trận khoảng cách / ma trận chi phí 2 chiều `cost[i][j]`**.

Lý do:

- TSP về bản chất là **đồ thị đầy đủ (Complete Graph)**: giữa 2 điểm bất kỳ đều có khoảng cách/chi phí di chuyển.
- Tra cứu chi phí từ điểm `i` sang điểm `j` bằng ma trận 2 chiều chỉ tốn thời gian **O(1)** (`cost[i][j]`), phù hợp cho các thuật toán phải truy vấn chi phí rất nhiều lần.

Quy ước: chương trình **không** tự nhân khoảng cách với đơn giá cố định. Nếu nhóm có dữ liệu gốc là khoảng cách (km), việc quy đổi sang chi phí phải thực hiện khi chuẩn bị file đầu vào, và ghi rõ cách quy đổi trong báo cáo. Cách chọn thang `fame` và giá trị `budget` cũng phải được giải thích trong báo cáo.

---

## 3. Môi trường phát triển

- Ngôn ngữ: Python 3.8 trở lên.
- Quản lý mã nguồn: Git và GitHub.
- Trình soạn thảo đề xuất: Visual Studio Code.
- Hệ điều hành: Windows, Linux hoặc macOS.
- Thư viện: Ưu tiên thư viện chuẩn Python; nếu sử dụng thư viện bên ngoài, phải ghi rõ trong tài liệu dự án.

Kiểm tra phiên bản Python:

```bash
python --version
```

Nếu hệ thống sử dụng lệnh `python3`, có thể thay `python` bằng `python3` trong các lệnh chạy chương trình.

---

## 4. Cấu trúc thư mục dự án

```text
my-tsp-project/
├── docs/
│   ├── Stage1_BaoCao_Greedy.docx
│   ├── Stage2_BaoCao_VetCan.docx
│   ├── Stage3_BaoCao_ChiaDeTri.docx
│   └── BaoCao_TongHop.docx
│
├── src/
│   ├── __init__.py
│   ├── utils.py
│   ├── stage1_greedy.py
│   ├── stage2_bruteforce.py
│   └── stage3_divide_conquer.py
│
├── tests/
│   └── input.txt
│
├── .gitignore
├── main.py
└── README.md
```

### Vai trò của từng thành phần

| Thành phần | Chức năng |
|---|---|
| `main.py` | Hiển thị menu, nhận lựa chọn và điều phối việc gọi thuật toán. |
| `src/utils.py` | Đọc dữ liệu, kiểm tra dữ liệu và cung cấp các hàm tính toán dùng chung. |
| `src/stage1_greedy.py` | Cài đặt thuật toán Greedy theo tỉ lệ độ nổi tiếng / chi phí. |
| `src/stage2_bruteforce.py` | Cài đặt DFS Backtracking kết hợp nhánh cận. |
| `src/stage3_divide_conquer.py` | Cài đặt phương pháp chia cụm, giải quyết cụm và kết hợp tuyến. |
| `tests/input.txt` | Chứa dữ liệu đầu vào phục vụ chạy thử và kiểm thử. |
| `docs/` | Chứa báo cáo từng Stage và báo cáo tổng hợp. |
| `README.md` | Hướng dẫn cài đặt, chạy chương trình và quy ước làm việc. |
| `.gitignore` | Khai báo các tệp và thư mục không cần đưa lên Git. |

File `src/__init__.py` có thể để trống. File này giúp thể hiện `src` là một package Python theo cách tổ chức truyền thống.

---

## 5. Quy ước dữ liệu đầu vào

### 5.1. Định dạng file `tests/input.txt`

- Dòng 1: Số nguyên `N`, là số lượng địa điểm.
- Dòng 2: Tên của `N` địa điểm, phân cách bằng dấu phẩy.
- Dòng 3: `N` giá trị độ nổi tiếng `fame`, phân cách bằng khoảng trắng (giá trị đầu tiên, của điểm `0`, phải bằng `0`).
- Dòng 4: Ngân sách `budget` (VNĐ).
- `N` dòng tiếp theo: Ma trận chi phí `N × N`, mỗi hàng đúng `N` số, phân cách bằng khoảng trắng.

Ví dụ:

```text
4
Ha Noi,Ha Long,Ninh Binh,Sa Pa
0 8 7 9
1500000
0 320000 180000 640000
320000 0 400000 900000
180000 400000 0 760000
640000 900000 760000 0
```

Đơn vị chi phí và ngân sách: **VNĐ**. Phiên bản đầu tiên sử dụng ma trận chi phí đối xứng, không âm và có đường chéo bằng 0.

Các quy tắc kiểm tra dữ liệu:

1. `N` phải là số nguyên dương.
2. Phải có đúng `N` tên địa điểm và đúng `N` giá trị `fame`.
3. `fame[i]` là số nguyên không âm; `fame[0] = 0`.
4. `budget` là số không âm.
5. Ma trận phải có đúng `N` hàng và mỗi hàng có đúng `N` phần tử.
6. Các giá trị chi phí phải không âm và `cost[i][i] = 0`.
7. Với bộ dữ liệu đối xứng, `cost[i][j]` phải bằng `cost[j][i]`.
8. Nếu dữ liệu không hợp lệ, chương trình phải thông báo lỗi rõ ràng thay vì tiếp tục tính toán.

Nếu sau này nhóm mở rộng sang đồ thị có hướng, cần điều chỉnh quy tắc kiểm tra và giải thích trong báo cáo.

### 5.2. Quy ước cấu trúc dữ liệu trong Python

Hàm đọc dữ liệu trong `src/utils.py` phải trả về năm giá trị theo đúng thứ tự:

```python
return n, locations, cost_matrix, fame, budget
```

Trong đó:

- `n`: Số lượng địa điểm.
- `locations`: Danh sách tên địa điểm theo thứ tự chỉ số.
- `cost_matrix`: Ma trận chi phí 2 chiều, truy cập bằng `cost_matrix[i][j]`.
- `fame`: Danh sách độ nổi tiếng theo chỉ số địa điểm.
- `budget`: Ngân sách tối đa.

Ví dụ sử dụng:

```python
n, locations, cost_matrix, fame, budget = load_data("tests/input.txt")
```

Địa điểm đầu tiên có chỉ số `0`, các địa điểm tiếp theo đánh số đến `N - 1`. Các thuật toán phải dùng cùng quy ước chỉ số này.

---

## 6. Quy ước tính chi phí và độ nổi tiếng

Với tuyến `path` (khép kín, bắt đầu và kết thúc tại `0`):

`total_cost = tổng cost_matrix[path[i]][path[i + 1]]` (gồm cả chặng quay về `0`)

`total_fame = tổng fame[v]` với mọi địa điểm `v` được thăm (mỗi địa điểm tính một lần)

Ví dụ với tuyến `[0, 2, 1, 0]`:

- `total_cost = cost[0][2] + cost[2][1] + cost[1][0]`
- `total_fame = fame[2] + fame[1]`

Tuyến hợp lệ khi `total_cost <= budget`. Không có đơn giá `cost_per_km` trong chương trình: chi phí đã nằm sẵn trong ma trận đầu vào.

---

## 7. Quy chuẩn kết quả đầu ra

Mọi thuật toán phải trả về đúng bốn giá trị theo thứ tự:

```python
return path, total_fame, total_cost, execution_time_ms
```

### 7.1. Ý nghĩa giá trị trả về

| Giá trị | Kiểu dữ liệu đề xuất | Ý nghĩa |
|---|---|---|
| `path` | `list[int]` | Danh sách chỉ số địa điểm được thăm, bắt đầu và kết thúc tại `0`. |
| `total_fame` | `int` | Tổng độ nổi tiếng của các điểm được thăm. |
| `total_cost` | `int` hoặc `float` | Tổng chi phí của tuyến (VNĐ), không vượt `budget`. |
| `execution_time_ms` | `float` | Thời gian thực thi, tính bằng mili giây. |

Khi thuật toán thành công:

- `path` bắt đầu và kết thúc bằng chỉ số `0`.
- Mỗi địa điểm được chọn xuất hiện đúng một lần giữa hai đầu; điểm xuất phát chỉ xuất hiện ở đầu và cuối.
- `total_cost <= budget`.
- `total_fame` và `total_cost` được tính theo chính `path` được trả về.
- Thời gian thực thi được đo bằng `time.perf_counter()`.

**Trường hợp không điểm nào nằm trong ngân sách:** nếu không có tuyến nào đi được ít nhất một địa điểm trong `budget`, chương trình phải thông báo rõ ràng ("ngân sách không đủ để thăm bất kỳ địa điểm nào") và trả về `path = [0]`, `total_fame = 0`, `total_cost = 0` kèm thông báo đó. Không được im lặng trả về kết quả rỗng như thể thuật toán đã thành công.

Nếu đầu vào không hợp lệ hoặc thuật toán gặp lỗi, chương trình phải báo lỗi hoặc dùng cơ chế kết quả thất bại đã được nhóm thống nhất.

### 7.2. Đo thời gian thực thi

```python
import time

start_time = time.perf_counter()

# Thuc hien phan viec can do thoi gian

execution_time_ms = (time.perf_counter() - start_time) * 1000
```

Quy ước đo:

- Dùng cùng một cách đo cho cả ba thuật toán, đơn vị mili giây (ms).
- Không tính thời gian người dùng nhập liệu hoặc chờ tương tác menu.
- Khi đo hiệu năng, nên chạy nhiều lần trên cùng dữ liệu và ghi rõ cách lấy kết quả trong báo cáo.
- Cần ghi nhận kích thước dữ liệu `N` và `budget` khi so sánh thời gian chạy.

### 7.3. Mẫu hiển thị trên Terminal

```text
============================================================
[STAGE 1] KẾT QUẢ THUẬT TOÁN: GREEDY (FAME / COST)
============================================================
Ngân sách: 1,500,000 VNĐ
Lộ trình chỉ số: 0 -> 2 -> 1 -> 0
Lộ trình địa điểm: Ha Noi -> Ninh Binh -> Ha Long -> Ha Noi
Tổng độ nổi tiếng: 15
Tổng chi phí: 900,000 VNĐ
Thời gian thực thi: 0.1234 ms
============================================================
```

Số liệu độ nổi tiếng và chi phí trong ví dụ được tính tay từ bộ dữ liệu ở Mục 5.1 (180,000 + 400,000 + 320,000 = 900,000; 7 + 8 = 15). Thời gian thực thi chỉ để minh họa định dạng.

---

## 8. Quy ước giao diện hàm giữa các module

Tất cả hàm có cùng chữ ký:

```python
solve_xxx(n, locations, cost_matrix, fame, budget)
```

### 8.1. Stage 1 – Greedy

File: `src/stage1_greedy.py`

```python
solve_greedy(n, locations, cost_matrix, fame, budget)
```

Nhiệm vụ:

1. Bắt đầu từ địa điểm `0`, tổng chi phí hiện tại bằng 0.
2. Trong các địa điểm chưa thăm `j` mà việc thêm `j` vẫn còn khả năng quay về `0` trong ngân sách (tức `chi_phí_hiện_tại + cost[cur][j] + cost[j][0] <= budget`), chọn điểm có `fame[j] / cost[cur][j]` lớn nhất.
3. Lặp lại đến khi không còn điểm nào thêm được.
4. Quay về `0`, tính `total_fame`, `total_cost` và thời gian thực thi.
5. Trả về bốn giá trị theo quy chuẩn.

Nhóm phải nêu rõ cách xử lý khi `cost[cur][j] = 0` (tránh chia cho 0) và quy tắc phá hòa khi hai điểm có cùng tỉ lệ. Đây là chiến lược nhanh nhưng **không** bảo đảm nghiệm tối ưu.

### 8.2. Stage 2 – Brute Force / Backtracking

File: `src/stage2_bruteforce.py`

```python
solve_bruteforce(n, locations, cost_matrix, fame, budget)
```

Nhiệm vụ:

1. Dùng DFS và đệ quy quay lui, tại mỗi nút của cây tìm kiếm đều xét tuyến hiện tại (nếu quay về `0` vẫn trong ngân sách) như một ứng viên nghiệm, vì tuyến không bắt buộc đi qua tất cả điểm.
2. Dùng mảng `visited[]` hoặc cấu trúc tương đương để đánh dấu địa điểm đã thăm.
3. Dùng nhánh cận để cắt các nhánh không thể cải thiện nghiệm tốt nhất, ví dụ:
   - Cắt khi chi phí đã tích lũy lớn hơn `budget` (ma trận chi phí không âm nên chi phí chỉ tăng thêm).
   - Cắt khi `fame_hiện_tại + tổng fame các điểm chưa thăm` nhỏ hơn `best_fame`.
   - Khi cận trên fame bằng `best_fame`, cắt nếu chi phí tích lũy đã lớn hơn hoặc bằng `best_cost`.
4. Trả về tuyến theo mục tiêu ở Mục 2.3 (tối đa `total_fame`, hòa thì `total_cost` nhỏ nhất).
5. Trả về bốn giá trị theo quy chuẩn.

Mọi điều kiện cắt nhánh phải được chứng minh trong báo cáo là không làm mất nghiệm tối ưu. Stage 2 đóng vai trò nghiệm tham chiếu cho các bộ dữ liệu đủ nhỏ. Do số tuyến tăng rất nhanh theo `N`, không kỳ vọng thuật toán này chạy nhanh với mọi kích thước dữ liệu.

### 8.3. Stage 3 – Divide & Conquer

File: `src/stage3_divide_conquer.py`

```python
solve_divide_conquer(n, locations, cost_matrix, fame, budget)
```

Các hàm nội bộ có thể gồm:

```python
divide_graph(...)
solve_sub_cluster(...)
combine_tours(...)
```

Nhiệm vụ:

1. Chia tập địa điểm thành các cụm nhỏ theo chiến lược đã chọn (dựa trên ma trận chi phí).
2. Chọn điểm và xác định thứ tự đi trong từng cụm; nhóm phải nêu rõ cách phân bổ ngân sách giữa các cụm.
3. Kết hợp các tuyến con thành một tuyến duy nhất.
4. Kiểm tra tuyến cuối: khép kín, mỗi điểm không lặp, và `total_cost <= budget`. Nếu vượt ngân sách sau khi ghép, phải có bước loại bớt điểm hoặc điều chỉnh để tuyến hợp lệ.
5. Tính `total_fame`, `total_cost` và thời gian thực thi.
6. Trả về bốn giá trị theo quy chuẩn.

**Lưu ý:** Chia tập điểm, giải từng cụm rồi ghép không tự động bảo đảm nghiệm tối ưu. Nhóm phải nêu rõ cách chia, cách phân bổ ngân sách, cách ghép, độ phức tạp dự kiến và giới hạn của phương pháp. Nếu chỉ là heuristic thì phải ghi rõ là phương pháp gần đúng trong báo cáo.

---

## 9. Chức năng của `src/utils.py`

`utils.py` chứa các hàm hỗ trợ dùng chung, không chứa logic tìm tuyến riêng của một Stage.

```python
load_data(file_path)
calculate_total_cost(path, cost_matrix)
calculate_total_fame(path, fame)
validate_tour(path, n, cost_matrix, budget)
```

- `load_data(file_path)`: đọc file, kiểm tra theo Mục 5.1 và trả về `n, locations, cost_matrix, fame, budget`.
- `calculate_total_cost(path, cost_matrix)`: cộng `cost_matrix[path[i]][path[i + 1]]` cho mọi chặng.
- `calculate_total_fame(path, fame)`: cộng `fame` của các điểm được thăm (không tính lặp điểm `0` ở cuối).
- `validate_tour(path, n, cost_matrix, budget)`: kiểm tra tuyến bắt đầu và kết thúc tại `0`, không lặp điểm, chỉ số hợp lệ và `total_cost <= budget`. Dùng chung cho kiểm thử và benchmark.

Các thành viên nên dùng các hàm chung này thay vì tự viết lại. Nếu cần đổi quy ước chung, phải thông báo và cập nhật cho cả nhóm.

---

## 10. Chức năng của `main.py`

Chạy chương trình từ thư mục gốc của dự án bằng:

```bash
python main.py
```

Menu chính:

```text
================ TSP PROJECT ================
1. Chay Stage 1 - Greedy
2. Chay Stage 2 - Brute Force / Backtracking
3. Chay Stage 3 - Divide & Conquer
4. Benchmark ca 3 thuat toan
0. Thoat
=============================================
Nhap lua chon:
```

`main.py` chịu trách nhiệm đọc dữ liệu, nhận lựa chọn, gọi hàm tương ứng và hiển thị kết quả. Không đặt toàn bộ logic ba thuật toán vào `main.py`. Nếu một Stage chưa triển khai, chương trình phải thông báo rõ thay vì hiển thị kết quả giả.

### Quy tắc benchmark

1. Dùng cùng một bộ dữ liệu (cùng `cost_matrix`, `fame`, `budget`) cho cả ba thuật toán.
2. Giữ nguyên điểm xuất phát.
3. Kiểm tra tính hợp lệ của từng tuyến (bằng `validate_tour`) trước khi so sánh.
4. So sánh theo thứ tự: `total_fame` cao hơn tốt hơn; nếu bằng nhau thì `total_cost` thấp hơn tốt hơn.
5. Đối chiếu với nghiệm tham chiếu của Stage 2 khi có thể.
6. Ghi lại thời gian chạy, `N` và `budget`.
7. Không kết luận một thuật toán tốt hơn chỉ dựa vào một lần chạy hoặc một bộ dữ liệu.
8. Nếu Stage 2 không chạy được với `N` lớn, phải ghi `N` đó là ngoài phạm vi đối chiếu nghiệm tối ưu bằng vét cạn; không tự suy ra nghiệm tối ưu từ Stage 1 hoặc Stage 3.

---

## 11. Hướng dẫn chạy chương trình

```bash
git clone <REPOSITORY_URL>
cd my-tsp-project
python main.py
```

1. Thay `<REPOSITORY_URL>` bằng URL repository GitHub của nhóm.
2. Đảm bảo `tests/input.txt` tồn tại và đúng định dạng ở Mục 5.
3. Nhập lựa chọn `1`, `2`, `3`, `4` hoặc `0` theo menu.
4. Kiểm tra lộ trình, tổng độ nổi tiếng, tổng chi phí và thời gian thực thi. Với dữ liệu nhỏ, đối chiếu kết quả của Greedy và Divide & Conquer với nghiệm tham chiếu của Stage 2.

---

## 12. Phân công nhiệm vụ (8 thành viên)

### Stage 1 – Greedy

**Thành viên 1 – Dữ liệu và tiện ích dùng chung**

- Phụ trách `src/utils.py`.
- Cài đặt `load_data()`, `calculate_total_cost()`, `calculate_total_fame()` và `validate_tour()`.
- Kiểm tra dữ liệu đầu vào (ma trận chi phí, `fame`, `budget`) và cung cấp dữ liệu thống nhất cho các Stage.
- Phối hợp với người tích hợp để thống nhất giao diện hàm.

**Thành viên 2 và Thành viên 3 – Greedy**

- Phụ trách `src/stage1_greedy.py`.
- Cài đặt Greedy theo tỉ lệ độ nổi tiếng / chi phí, có kiểm tra ngân sách (kể cả chặng quay về `0`).
- Kiểm thử trên bộ dữ liệu mẫu và các bộ bổ sung.
- Hoàn thiện báo cáo Stage 1.

### Stage 2 – Brute Force / Backtracking

**Thành viên 4 và Thành viên 5 – Vét cạn và nhánh cận**

- Phụ trách `src/stage2_bruteforce.py`.
- Cài đặt DFS Backtracking với `visited[]`, xét ứng viên nghiệm tại mọi nút.
- Thiết kế, chứng minh và kiểm thử điều kiện nhánh cận.
- Kiểm tra tính tối ưu trên các bộ dữ liệu nhỏ có thể kiểm chứng.
- Phân tích độ phức tạp và giới hạn thực thi.
- Hoàn thiện báo cáo Stage 2.

### Stage 3 – Divide & Conquer

**Thành viên 6 – Divide và Conquer**

- Phụ trách phần chia đồ thị thành cụm, phân bổ ngân sách và chọn điểm trong từng cụm.
- Đề xuất cấu trúc dữ liệu và chiến lược chia cụm.
- Phối hợp với Thành viên 7 để thống nhất định dạng kết quả trung gian.

**Thành viên 7 – Combine và kiểm thử**

- Phụ trách hàm kết hợp các tuyến con và tích hợp Stage 3.
- Bảo đảm tuyến kết quả khép kín, không lặp điểm và không vượt ngân sách.
- Kiểm thử tính hợp lệ, đo thời gian và phân tích hạn chế của phương pháp.
- Phối hợp hoàn thiện báo cáo Stage 3.

### Tích hợp, benchmark và báo cáo tổng hợp

**Thành viên 8 – Tích hợp và thực nghiệm**

- Phụ trách tích hợp `main.py`, menu và benchmark; phối hợp với các thành viên từng module.
- Xây dựng bộ kiểm thử dùng chung và ghi nhận kết quả thực nghiệm.
- Tổng hợp bảng so sánh thời gian chạy, tổng độ nổi tiếng, tổng chi phí và chất lượng lời giải.
- Tổng hợp các báo cáo Stage thành `docs/BaoCao_TongHop.docx`.

Thành viên 8 không được tự giả định rằng Divide & Conquer đã tìm được nghiệm tối ưu; các kết luận phải dựa trên kết quả kiểm thử.

**Lưu ý:** Phân công trên là phân công chính. Các thành viên vẫn cần hỗ trợ kiểm thử chéo và rà soát mã nguồn của nhau.

---

## 13. Quy trình quản lý mã nguồn bằng Git/GitHub

### 13.1. Quy tắc chung

- `main` chứa phiên bản đã được kiểm tra và tích hợp.
- Không tự ý commit trực tiếp lên `main`.
- Mỗi phần việc được thực hiện trên một nhánh riêng.
- Một Pull Request nên tập trung vào một phần việc cụ thể.
- Trước khi merge, cần xem thay đổi, kiểm thử và xử lý xung đột nếu có.
- Không commit mật khẩu, token, thông tin xác thực hoặc tệp môi trường cá nhân.

### 13.2. Quy ước đặt tên nhánh

```text
feature/utils-data-loader
feature/stage1-greedy
feature/stage2-bruteforce
feature/stage3-divide-conquer
feature/main-benchmark
docs/stage1-report
docs/stage2-report
docs/stage3-report
docs/final-report
```

Tên nhánh có thể điều chỉnh theo phần việc thực tế, nhưng phải dễ hiểu và không trùng với nhánh của người khác.

### 13.3. Tạo nhánh làm việc

```bash
git switch main
git pull origin main
git switch -c feature/stage1-greedy
```

Đổi tên nhánh theo phần việc được giao.

### 13.4. Commit và push

```bash
git add src/stage1_greedy.py
git commit -m "Implement greedy fame/cost algorithm"
git push -u origin feature/stage1-greedy
```

Chỉ đưa các tệp liên quan đến phần việc của mình vào commit.

### 13.5. Tạo Pull Request

1. Mở repository trên GitHub.
2. Tạo Pull Request từ nhánh tính năng vào `main`.
3. Mô tả phần đã hoàn thành và cách kiểm thử.
4. Nhờ người phụ trách tích hợp hoặc thành viên khác rà soát.
5. Chỉ merge sau khi thay đổi đã được kiểm tra.

Nếu nhiều người làm cùng một Stage, cần thống nhất quyền sở hữu file và chia nhiệm vụ theo hàm hoặc phần việc để giảm xung đột.

### 13.6. Quy tắc làm việc với báo cáo Word

- Mỗi Stage có một file báo cáo riêng.
- Mỗi người cập nhật báo cáo trên nhánh của mình và gửi Pull Request.
- Không để nhiều thành viên cùng chỉnh sửa một file `.docx` cùng lúc nếu có thể tránh.
- Thành viên tổng hợp chịu trách nhiệm hợp nhất nội dung và kiểm tra định dạng.
- Sau khi báo cáo tổng hợp hoàn tất, đưa `BaoCao_TongHop.docx` vào `docs/`.

Do `.docx` là tệp nhị phân, Git thường không thể hợp nhất nội dung bên trong như với file `.py`. Vì vậy, nhóm nên chia báo cáo theo Stage và chỉ có một người chịu trách nhiệm ghép bản cuối.

---

## 14. Quy trình kiểm thử

Mỗi thuật toán cần được kiểm thử ít nhất trên các trường hợp sau:

1. Bộ dữ liệu mẫu 4 địa điểm (Mục 5.1, `budget = 1,500,000`): nghiệm tối ưu là đi `Ha Noi -> Ninh Binh -> Ha Long -> Ha Noi`, `total_fame = 15`, `total_cost = 900,000` (đã tính tay bằng cách xét mọi tập điểm).
2. Cùng dữ liệu nhưng `budget = 1,600,000`: nghiệm tối ưu đổi thành đi qua Ninh Binh và Sa Pa, `total_fame = 16`, `total_cost = 1,580,000`. Greedy theo tỉ lệ fame/cost sẽ chọn Ninh Binh rồi Ha Long (`total_fame = 15`), nên đây là ca kiểm thử cho thấy Greedy không tối ưu. Nhóm cần ghi nhận kết quả thực tế của từng thuật toán.
3. Ngân sách đủ lớn để đi qua tất cả địa điểm: kết quả phải thăm hết mọi điểm; Stage 2 phải cho tuyến có chi phí nhỏ nhất (trở về TSP chuẩn).
4. Ngân sách quá nhỏ, không điểm nào đi được: phải có thông báo rõ ràng theo Mục 7.1.
5. Ngân sách đúng bằng chi phí của một tuyến (kiểm tra điều kiện biên `<=`).
6. Hai tuyến có cùng `total_fame`: phải chọn tuyến có `total_cost` nhỏ hơn.
7. Bộ dữ liệu nhỏ khác có thể xác định nghiệm tối ưu bằng vét cạn.
8. Bộ dữ liệu nhiều địa điểm hơn để quan sát thời gian thực thi.
9. Dữ liệu sai: sai số lượng tên, sai số lượng `fame`, `fame[0] != 0`, sai kích thước ma trận, giá trị âm.
10. Nhiều điểm có cùng tỉ lệ hoặc cùng chi phí nhỏ nhất (kiểm tra quy tắc phá hòa).

Các tiêu chí kiểm tra:

- Tuyến bắt đầu và kết thúc tại `0`, không lặp điểm.
- `total_cost <= budget`.
- `total_fame`, `total_cost` khớp với phép tính từ `fame`, `cost_matrix` và tuyến.
- Thời gian chạy được đo bằng `time.perf_counter()`.
- Các thuật toán dùng cùng quy ước dữ liệu.
- Kết quả benchmark được ghi lại trung thực, kể cả khi một thuật toán chạy chậm hoặc cho kết quả kém hơn.

---

## 15. Sản phẩm cần bàn giao

1. Mã nguồn của ba thuật toán.
2. Module tiện ích đọc dữ liệu và tính toán dùng chung.
3. Chương trình `main.py` có menu chạy từng Stage và benchmark.
4. Bộ dữ liệu kiểm thử (ma trận chi phí, `fame`, `budget`) và hướng dẫn định dạng dữ liệu.
5. Báo cáo riêng cho Stage 1, Stage 2 và Stage 3.
6. Báo cáo tổng hợp so sánh các thuật toán.
7. Bảng kết quả thực nghiệm có kích thước dữ liệu, ngân sách, tổng độ nổi tiếng, tổng chi phí và thời gian chạy.
8. Lịch sử commit và Pull Request thể hiện quá trình cộng tác.

## 16. Kết luận

Dự án hướng đến việc kết hợp kiến thức giải thuật với kỹ năng lập trình, kiểm thử, phân tích hiệu năng và cộng tác bằng Git/GitHub.

Tất cả thành viên phải tuân thủ quy ước dữ liệu (ma trận chi phí `cost[i][j]`, độ nổi tiếng `fame`, ngân sách `budget`), giao diện hàm và định dạng kết quả để bảo đảm các module tích hợp được. Mọi kết luận về tính tối ưu và hiệu năng phải dựa trên thuật toán thực tế, bộ dữ liệu kiểm thử và kết quả đo được.
