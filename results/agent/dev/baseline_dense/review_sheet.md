# Review sheet — dev / baseline_dense

Model claude-haiku-5-5, method dense, top-k 3, budget 6000 ký tự, max_searches 3, neighbors False, effort medium.

## d01 · truc_tiep · có đáp án · status `answered`
**Hỏi:** Ngày Quyền của người tiêu dùng Việt Nam là ngày nào?

**Đáp án chuẩn:** Ngày 15 tháng 3 hằng năm.
**Gold:** [{'source_id': 'luat19_2023', 'page': 12, 'evidence': 'Ngày 15 tháng 3 hằng năm là Ngày Quyền của người tiêu dùng Việt Nam.'}]

- search `Ngày Quyền của người tiêu dùng Việt Nam` → mới: C1, C2, C3

**Agent:** Ngày Quyền của người tiêu dùng Việt Nam là ngày 15 tháng 3 hằng năm [struct1000:luat19_2023:p12:o24008:35e7a6e2d5]. Việc tổ chức hoạt động hưởng ứng được thực hiện hằng năm, cao điểm từ ngày 01 đến ngày 20 tháng 3 [struct1000:nd55_2024:p2:o2744:6f88093140][struct1000:nd55_2024:p3:o4320:a84ba2c728].

> `struct1000:luat19_2023:p12:o24008:35e7a6e2d5` (trang 12): [Luật 19/2023/QH15 · Chương I · Điều 13]
Điều 13. Ngày Quyền của người tiêu dùng Việt Nam
1. Ngày 15 tháng 3 hằng năm là Ngày Quyền của người tiêu dùng Việt Nam.
2. Chính phủ quy định việc tổ chức thực hiện các hoạt động hưởng ứng Ngày
Quyền của người tiêu dùng Việt Nam.

> `struct1000:nd55_2024:p2:o2744:6f88093140` (trang 2,3): [Nghị định 55/2024/NĐ-CP · Chương II · Điều 3]
1. Ngày Quyền của người tiêu dùng Việt Nam được tổ chức hằng năm nhằm:
a) Khẳng định vai trò, vị trí, tầm quan trọng của công tác bảo vệ quyền lợi người
tiêu dùng với sự phát triển ổn định, bền vững của xã hội và đất nước;
b) Tuyên truyền, giáo dục, phổ biến pháp luật và các chính sách về bảo vệ quyền
lợi người tiêu dùng;
c) Tạo cơ sở để huy động, tập trung nguồn lực, sự quan tâm, hưởng ứng, tham
gia của toàn xã hội đối với công tác bảo vệ quyền lợi người tiêu dùng;
d) Góp phần xây dựng một môi trường tiêu dùng lành mạnh cho cả người tiêu
dùng và 

> `struct1000:nd55_2024:p3:o4320:a84ba2c728` (trang 3): [Nghị định 55/2024/NĐ-CP · Chương II · Điều 3]
3. Kế hoạch tổ chức hoạt động hưởng ứng
a) Bộ Công Thương chủ trì, phối hợp với các bộ, ngành có liên quan và Ủy ban
nhân dân các tỉnh, thành phố trực thuộc Trung ương, cơ quan, tổ chức, cá nhân có
liên quan lựa chọn chủ đề phát động, xây dựng kế hoạch triển khai cụ thể; hướng
dẫn, chỉ đạo, tổ chức thực hiện Ngày Quyền của người tiêu dùng Việt Nam hằng
năm, bảo đảm thiết thực, hiệu quả, tiết kiệm;
b) Kế hoạch tổ chức hoạt động hưởng ứng Ngày Quyền của người tiêu dùng
Việt Nam được thực hiện thường xuyên, liên tục trong cả năm, đặc biệt tập trung
v

_auto: context có evidence = True, citation chứa evidence = True_

---

## d02 · dien_dat_lai · có đáp án · status `answered`
**Hỏi:** Phụ nữ nuôi con nhỏ dưới bao nhiêu tháng tuổi thì được xếp vào nhóm người tiêu dùng dễ bị tổn thương?

**Đáp án chuẩn:** Phụ nữ đang mang thai hoặc nuôi con dưới 36 tháng tuổi.
**Gold:** [{'source_id': 'luat19_2023', 'page': 6, 'evidence': 'Phụ nữ đang mang thai hoặc nuôi con dưới 36 tháng tuổi'}]

- search `người tiêu dùng dễ bị tổn thương phụ nữ nuôi con nhỏ dưới 36 tháng tuổi` → mới: C1, C2, C3
- search `người tiêu dùng dễ bị tổn thương bao gồm phụ nữ nuôi con nhỏ` → mới: C4

**Agent:** Theo Luật 19/2023/QH15 (Điều 8), phụ nữ nuôi con dưới 36 tháng tuổi (cùng với phụ nữ đang mang thai) thuộc nhóm người tiêu dùng dễ bị tổn thương [struct1000:luat19_2023:p6:o10517:57d9d82ab1]. Đây là quy định của luật hiện hành; luật cũ (Luật 59/2010/QH12) không thuộc phạm vi câu trả lời này.

> `struct1000:luat19_2023:p6:o10517:57d9d82ab1` (trang 6): [Luật 19/2023/QH15 · Chương I · Điều 8]
Điều 8. Bảo vệ quyền lợi người tiêu dùng dễ bị tổn thương
1. Người tiêu dùng dễ bị tổn thương là người tiêu dùng có khả năng chịu nhiều
tác động bất lợi về tiếp cận thông tin, sức khỏe, tài sản, giải quyết tranh chấp tại
thời điểm mua hoặc sử dụng sản phẩm, hàng hóa, dịch vụ, bao gồm:
a) Người cao tuổi theo quy định của pháp luật về người cao tuổi;
b) Người khuyết tật theo quy định của pháp luật về người khuyết tật;
c) Trẻ em theo quy định của pháp luật về trẻ em;
d) Người dân tộc thiểu số; người sinh sống tại vùng đồng bào dân tộc thiểu số
và miền núi, 

_auto: context có evidence = True, citation chứa evidence = True_

---

## d03 · truc_tiep · có đáp án · status `answered`
**Hỏi:** Sau khi nhận được yêu cầu thương lượng của người tiêu dùng, doanh nghiệp phải tiến hành thương lượng trong thời hạn bao lâu?

**Đáp án chuẩn:** Trong thời hạn 07 ngày làm việc kể từ ngày nhận được yêu cầu (Luật 2010 ghi 'không quá 07 ngày làm việc').
**Gold:** [{'source_id': 'luat19_2023', 'page': 43, 'evidence': 'tiếp nhận, tiến hành thương lượng với người tiêu dùng trong thời hạn 07 ngày làm việc kể từ ngày nhận được yêu cầu'}, {'source_id': 'luat59_2010', 'page': 15, 'evidence': 'tiếp nhận, tiến hành thương lượng với người tiêu dùng trong thời hạn không quá 07 ngày làm việc, kể từ ngày nhận được yêu cầu'}]

- search `thời hạn thương lượng giữa người tiêu dùng và tổ chức, cá nhân kinh doanh sau khi nhận yêu cầu` → mới: C1, C2, C3
- search `yêu cầu thương lượng người tiêu dùng doanh nghiệp phải thương lượng trong thời hạn ngày` → mới: —

**Agent:** Theo Luật 19/2023/QH15 (hiện hành), tổ chức, cá nhân kinh doanh có trách nhiệm tiếp nhận và tiến hành thương lượng với người tiêu dùng trong thời hạn 07 ngày làm việc kể từ ngày nhận được yêu cầu [struct1000:luat19_2023:p42:o81740:66655aa907]. Sau khi kết thúc thương lượng, doanh nghiệp phải thông báo bằng văn bản kết quả cho cơ quan quản lý nhà nước và tổ chức xã hội tham gia bảo vệ quyền lợi người tiêu dùng trong 05 ngày làm việc [struct1000:luat19_2023:p43:o82591:0d1b9f0358]. Nếu từ chối yêu cầu thương lượng, doanh nghiệp phải trả lời bằng văn bản, nêu rõ lý do trong 07 ngày làm việc [struct1000:luat19_2023:p43:o82591:0d1b9f0358]. Lưu ý: Luật 59/2010/QH12 cũng quy định thời hạn tương tự là không quá 07 ngày làm việc [struct1000:luat59_2010:p15:o28317:6ebef7a16b], nhưng luật 2010 đã được thay thế.

> `struct1000:luat59_2010:p15:o28317:6ebef7a16b` (trang 15): [Luật 59/2010/QH12 · Chương IV · Điều 31]
Mục 1
THƯƠNG LƯỢNG
Điều 31. Thương lượng
1. Người tiêu dùng có quyền gửi yêu cầu đến tổ chức, cá nhân kinh doanh hàng
hóa, dịch vụ để thương lượng khi cho rằng quyền, lợi ích hợp pháp của mình bị
xâm phạm.
2. Tổ chức, cá nhân kinh doanh hàng hóa, dịch vụ có trách nhiệm tiếp nhận, tiến
hành thương lượng với người tiêu dùng trong thời hạn không quá 07 ngày làm việc,
kể từ ngày nhận được yêu cầu.

> `struct1000:luat19_2023:p43:o82591:0d1b9f0358` (trang 43): [Luật 19/2023/QH15 · Chương V · Điều 57]
4. Trong thời hạn 07 ngày làm việc kể từ ngày nhận được yêu cầu của người
tiêu dùng, cơ quan quản lý nhà nước về bảo vệ quyền lợi người tiêu dùng, tổ chức
xã hội tham gia bảo vệ quyền lợi người tiêu dùng có trách nhiệm chuyển yêu cầu
của người tiêu dùng đến tổ chức, cá nhân kinh doanh được yêu cầu thương lượng.
5. Tổ chức, cá nhân kinh doanh có trách nhiệm tiến hành thương lượng với
người tiêu dùng trong thời hạn 07 ngày làm việc kể từ ngày nhận được yêu cầu và
thông báo bằng văn bản kết quả thương lượng đến cơ quan quản lý nhà nước về
bảo vệ quyền lợi 

> `struct1000:luat19_2023:p42:o81740:66655aa907` (trang 42,43): [Luật 19/2023/QH15 · Chương V · Điều 57]
Điều 57. Trình tự, thủ tục thương lượng
1. Người tiêu dùng gửi yêu cầu thương lượng và thông tin, tài liệu liên quan
(nếu có) đến tổ chức, cá nhân kinh doanh tại trụ sở chính, chi nhánh, văn phòng đại
diện, địa điểm kinh doanh, trang thông tin điện tử hoặc thông qua phương thức liên
lạc khác do tổ chức, cá nhân kinh doanh đã công khai hoặc đang áp dụng.
2. Tổ chức, cá nhân kinh doanh có trách nhiệm tiếp nhận, tiến hành thương
lượng với người tiêu dùng trong thời hạn 07 ngày làm việc kể từ ngày nhận được
yêu cầu.
3. Trong trường hợp quy định tại khoản 3 

_auto: context có evidence = True, citation chứa evidence = True_

---

## d04 · dieu_kien · có đáp án · status `answered`
**Hỏi:** Vụ án dân sự về bảo vệ quyền lợi người tiêu dùng có giá trị giao dịch bao nhiêu thì được giải quyết theo thủ tục rút gọn mà không phải đáp ứng điều kiện tại khoản 1 Điều 317 Bộ luật Tố tụng dân sự?

**Đáp án chuẩn:** Giá trị giao dịch dưới 100 triệu đồng.
**Gold:** [{'source_id': 'luat19_2023', 'page': 48, 'evidence': 'có giá trị giao dịch dưới 100 triệu đồng thì được giải quyết theo thủ tục rút gọn'}, {'source_id': 'luat19_2023', 'page': 53, 'evidence': 'có giá trị giao dịch dưới 100 triệu đồng được thực hiện theo quy định tại khoản 2 Điều 70'}]

- search `vụ án dân sự bảo vệ quyền lợi người tiêu dùng giải quyết theo thủ tục rút gọn không phải đáp ứng điều kiện khoản 1 Điều 317 Bộ luật Tố tụng dân sự` → mới: C1, C2, C3
- search `thủ tục rút gọn tranh chấp người tiêu dùng giá trị giao dịch dưới triệu đồng` → mới: —

**Agent:** Vụ án dân sự về bảo vệ quyền lợi người tiêu dùng có giá trị giao dịch dưới 100 triệu đồng được giải quyết theo thủ tục rút gọn mà không phải đáp ứng các điều kiện quy định tại khoản 1 Điều 317 Bộ luật Tố tụng dân sự [struct1000:luat19_2023:p48:o90657:402750c2ce]. Quy định này được Luật 19/2023/QH15 bổ sung tại khoản 5 Điều 317 BLTTDS, dẫn chiếu đến khoản 2 Điều 70 của Luật Bảo vệ quyền lợi người tiêu dùng [struct1000:luat19_2023:p53:o101188:c6c8fea761]. Vụ án có giá trị giao dịch từ 100 triệu đồng trở lên chỉ được giải quyết theo thủ tục rút gọn khi đáp ứng đủ các điều kiện tại khoản 1 Điều 317 BLTTDS [struct1000:luat19_2023:p48:o90657:402750c2ce]. Lưu ý: Luật 59/2010/QH12 trước đây cũng quy định ngưỡng dưới 100 triệu đồng nhưng theo thủ tục đơn giản, với thêm điều kiện người khởi kiện là cá nhân và vụ án đơn giản, chứng cứ rõ ràng [struct1000:luat59_2010:p17:o31167:936f1ed697].

> `struct1000:luat19_2023:p48:o90657:402750c2ce` (trang 48): [Luật 19/2023/QH15 · Chương V · Điều 70]
Mục 5
GIẢI QUYẾT TRANH CHẤP TẠI TÒA ÁN
Điều 70. Vụ án dân sự về bảo vệ quyền lợi người tiêu dùng
1. Vụ án dân sự về bảo vệ quyền lợi người tiêu dùng là vụ án mà bên khởi kiện
là người tiêu dùng hoặc tổ chức xã hội tham gia bảo vệ quyền lợi người tiêu dùng
theo quy định tại Luật này. Tòa án giải quyết vụ án dân sự về bảo vệ quyền lợi
người tiêu dùng theo trình tự, thủ tục quy định tại Bộ luật Tố tụng dân sự.
2. Vụ án dân sự về bảo vệ quyền lợi người tiêu dùng có giá trị giao dịch dưới
100 triệu đồng thì được giải quyết theo thủ tục rút gọn mà không phải 

> `struct1000:luat19_2023:p53:o101188:c6c8fea761` (trang 53): [Luật 19/2023/QH15 · Chương VII · Điều 78]
2. Sửa đổi, bổ sung một số khoản của Điều 317 như sau:
a) Sửa đổi, bổ sung đoạn mở đầu khoản 1 như sau:
“1. Trừ trường hợp quy định tại khoản 5 Điều này, Tòa án giải quyết vụ án
theo thủ tục rút gọn khi có đủ các điều kiện sau đây:”;
b) Bổ sung khoản 5 vào sau khoản 4 như sau:
“5. Điều kiện áp dụng thủ tục rút gọn trong việc giải quyết vụ án dân sự về
bảo vệ quyền lợi người tiêu dùng có giá trị giao dịch dưới 100 triệu đồng được
thực hiện theo quy định tại khoản 2 Điều 70 của Luật Bảo vệ quyền lợi người
tiêu dùng.”.

> `struct1000:luat59_2010:p17:o31167:936f1ed697` (trang 17): [Luật 59/2010/QH12 · Chương IV · Điều 41]
Mục 4
GIẢI QUYẾT TRANH CHẤP TẠI TÒA ÁN
Điều 41. Vụ án dân sự về bảo vệ quyền lợi người tiêu dùng
1. Vụ án dân sự về bảo vệ quyền lợi người tiêu dùng là vụ án mà bên khởi kiện
là người tiêu dùng hoặc tổ chức xã hội tham gia bảo vệ quyền lợi người tiêu dùng
theo quy định của Luật này.
2. Vụ án dân sự về bảo vệ quyền lợi người tiêu dùng được giải quyết theo thủ tục
đơn giản quy định trong pháp luật về tố tụng dân sự khi có đủ các điều kiện sau đây:
a) Cá nhân là người tiêu dùng khởi kiện; tổ chức, cá nhân trực tiếp cung cấp
hàng hóa, dịch vụ cho người tiê

_auto: context có evidence = True, citation chứa evidence = True_

---

## d05 · metadata_filter · có đáp án · status `answered`
**Hỏi:** Theo quy định cũ (giao dịch xác lập năm 2015), khi giao kết hợp đồng từ xa mà doanh nghiệp cung cấp thông tin không đầy đủ, người tiêu dùng có bao nhiêu ngày để đơn phương chấm dứt hợp đồng?

**Đáp án chuẩn:** Mười (10) ngày kể từ ngày giao kết hợp đồng.
**Gold:** [{'source_id': 'nd99_2011', 'page': 7, 'evidence': 'trong thời hạn mười (10) ngày kể từ ngày giao kết hợp đồng người tiêu dùng có quyền đơn phương chấm dứt thực hiện hợp đồng'}]

- search `hợp đồng từ xa cung cấp thông tin không đầy đủ người tiêu dùng đơn phương chấm dứt hợp đồng` → mới: C1, C2, C3
- search `giao kết hợp đồng từ xa quyền chấm dứt hợp đồng trong thời hạn ngày` → mới: —

**Agent:** Theo Nghị định 99/2011/NĐ-CP (Điều 17, khoản 3), trừ trường hợp các bên có thỏa thuận khác, nếu tổ chức, cá nhân kinh doanh cung cấp không đúng, không đầy đủ thông tin theo quy định, người tiêu dùng có 10 ngày kể từ ngày giao kết hợp đồng để đơn phương chấm dứt thực hiện hợp đồng và thông báo cho tổ chức, cá nhân kinh doanh [struct1000:nd99_2011:p7:o13693:0ff33631c9]. Người tiêu dùng không phải trả chi phí liên quan đến việc chấm dứt, chỉ phải trả chi phí đối với phần hàng hóa, dịch vụ đã sử dụng [struct1000:nd99_2011:p7:o13693:0ff33631c9]. Khi người tiêu dùng đơn phương chấm dứt, doanh nghiệp phải trả lại tiền chậm nhất trong 30 ngày kể từ ngày người tiêu dùng tuyên bố chấm dứt; quá hạn phải trả lãi theo lãi suất cơ bản do Ngân hàng Nhà nước công bố [struct1000:nd99_2011:p7:o14386:459856d615].

Lưu ý: Đoạn tài liệu tìm được không ghi rõ tiêu đề của Điều 17 là "giao kết hợp đồng từ xa"; quy định trên được trích từ Điều 17 về việc giao kết hợp đồng qua phương tiện từ xa. Quy định 3 ngày làm việc tại Điều 19 [struct1000:nd99_2011:p9:o17584:7d4370b572] áp dụng riêng cho bán hàng tận cửa, không phải cho hợp đồng từ xa nói chung.

> `struct1000:nd99_2011:p7:o13693:0ff33631c9` (trang 7): [Nghị định 99/2011/NĐ-CP · Chương III · Điều 17]
2. Trường hợp việc đề nghị giao kết hợp đồng được thực hiện thông qua điện
thoại, tổ chức, cá nhân kinh doanh cần phải nói rõ ngay từ đầu về tên, địa chỉ của
mình và mục đích của cuộc đàm thoại.
3. Trừ trường hợp các bên có thỏa thuận khác, trong trường hợp tổ chức, cá
nhân kinh doanh cung cấp không đúng, không đầy đủ thông tin quy định tại khoản
1 Điều này thì trong thời hạn mười (10) ngày kể từ ngày giao kết hợp đồng người
tiêu dùng có quyền đơn phương chấm dứt thực hiện hợp đồng đã giao kết và thông
báo cho tổ chức, cá nhân kinh doanh. Người 

> `struct1000:nd99_2011:p9:o17584:7d4370b572` (trang 9): [Nghị định 99/2011/NĐ-CP · Chương III · Điều 19]
3. Trong thời hạn ba (03) ngày làm việc kể từ ngày giao kết hợp đồng, người
tiêu dùng có quyền yêu cầu đơn phương chấm dứt thực hiện hợp đồng đã giao kết và
thông báo bằng văn bản cho tổ chức, cá nhân kinh doanh. Trước khi hết thời hạn
này, người bán hàng tận cửa không được phép yêu cầu người tiêu dùng thanh toán
hoặc thực hiện các nội dung hợp đồng, trừ trường hợp pháp luật có quy định khác.
4. Trường hợp hợp đồng bán hàng tận cửa được lập thành văn bản, khi ký kết
hợp đồng bán hàng tận cửa, người tiêu dùng phải tự ghi ngày, tháng giao kết hợp


> `struct1000:nd99_2011:p7:o14386:459856d615` (trang 7): [Nghị định 99/2011/NĐ-CP · Chương III · Điều 17]
4. Trường hợp người tiêu dùng đơn phương chấm dứt thực hiện hợp đồng theo
quy định tại khoản 3 Điều này, tổ chức, cá nhân kinh doanh phải trả lại tiền cho
người tiêu dùng chậm nhất là ba mươi (30) ngày kể từ ngày người tiêu dùng tuyên
bố đơn phương chấm dứt thực hiện hợp đồng. Quá thời hạn này, tổ chức, cá nhân
kinh doanh phải trả lãi đối với số tiền chậm trả theo lãi suất cơ bản do Ngân hàng
Nhà nước công bố tương ứng với thời gian chậm trả tại thời điểm thanh toán. Việc
hoàn trả được thực hiện theo phương thức mà người tiêu dùng đã thanh toán,

_auto: context có evidence = True, citation chứa evidence = True_

---

## d06 · metadata_filter · có đáp án · status `answered`
**Hỏi:** Theo quy định hiện hành, nếu doanh nghiệp giao dịch từ xa cung cấp thông tin không chính xác hoặc không đầy đủ, người tiêu dùng có bao lâu để đơn phương chấm dứt hợp đồng?

**Đáp án chuẩn:** Trong thời hạn 30 ngày kể từ ngày giao kết hợp đồng.
**Gold:** [{'source_id': 'luat19_2023', 'page': 30, 'evidence': 'Trong thời hạn 30 ngày kể từ ngày giao kết hợp đồng, đơn phương chấm dứt thực hiện hợp đồng đã giao kết'}]

- search `giao dịch từ xa cung cấp thông tin không chính xác không đầy đủ người tiêu dùng đơn phương chấm dứt hợp đồng` → mới: C1, C2, C3
- search `quyền chấm dứt hợp đồng giao dịch điện tử thông tin không đầy đủ thời hạn 7 ngày 90 ngày` → mới: C4, C5

**Agent:** Theo Luật 19/2023/QH15 (Điều 38 khoản 3 điểm b), khi tổ chức, cá nhân kinh doanh cung cấp không chính xác hoặc không đầy đủ thông tin quy định tại khoản 1 Điều 37, người tiêu dùng có quyền đơn phương chấm dứt thực hiện hợp đồng đã giao kết trong thời hạn 30 ngày kể từ ngày giao kết hợp đồng và phải thông báo cho tổ chức, cá nhân kinh doanh [struct1000:luat19_2023:p30:o57562:6c1cde9790]. Người tiêu dùng không phải trả bất kỳ chi phí nào để chấm dứt hợp đồng, trừ chi phí đối với phần sản phẩm, hàng hóa, dịch vụ đã sử dụng [struct1000:luat19_2023:p30:o57562:6c1cde9790]. Ngoài ra, người tiêu dùng có quyền thỏa thuận cách xử lý hợp đồng hoặc yêu cầu cơ quan có thẩm quyền tuyên bố hợp đồng vô hiệu hoặc hủy bỏ theo pháp luật dân sự [struct1000:luat19_2023:p30:o57562:6c1cde9790]. Lưu ý: nguồn đã tìm được không nêu rõ thời hạn này được tính từ thời điểm nào nếu hợp đồng giao kết qua giao dịch từ xa, ngoài mốc "ngày giao kết hợp đồng" nêu trên.

> `struct1000:luat19_2023:p30:o57562:6c1cde9790` (trang 30): [Luật 19/2023/QH15 · Chương III · Điều 38]
3. Trường hợp tổ chức, cá nhân kinh doanh cung cấp không chính xác hoặc
không đầy đủ thông tin quy định tại khoản 1 Điều 37 của Luật này, người tiêu
dùng có quyền sau đây:
a) Thỏa thuận lựa chọn cách thức xử lý hợp đồng với tổ chức, cá nhân
kinh doanh;
b) Trong thời hạn 30 ngày kể từ ngày giao kết hợp đồng, đơn phương chấm
dứt thực hiện hợp đồng đã giao kết và thông báo cho tổ chức, cá nhân kinh
doanh. Người tiêu dùng không phải trả bất kỳ chi phí nào dưới mọi hình thức để
chấm dứt thực hiện hợp đồng, trừ chi phí đối với phần sản phẩm, hàng hóa, dịch


_auto: context có evidence = True, citation chứa evidence = True_

---

## d07 · metadata_filter · có đáp án · status `answered`
**Hỏi:** Theo Nghị định 99/2011, một công dân muốn làm hòa giải viên tranh chấp tiêu dùng cần tối thiểu bao nhiêu năm kinh nghiệm công tác?

**Đáp án chuẩn:** Ít nhất năm (05) năm kinh nghiệm công tác.
**Gold:** [{'source_id': 'nd99_2011', 'page': 13, 'evidence': 'Có ít nhất năm (05) năm kinh nghiệm công tác'}]

- search `điều kiện hòa giải viên tranh chấp tiêu dùng số năm kinh nghiệm công tác Nghị định 99/2011` → mới: C1, C2, C3

**Agent:** Theo Nghị định 99/2011/NĐ-CP, công dân Việt Nam muốn làm Hòa giải viên phải có đủ các điều kiện: có năng lực hành vi dân sự đầy đủ, có phẩm chất đạo đức tốt, trung thực, và có ít nhất 05 năm kinh nghiệm công tác [struct1000:nd99_2011:p13:o26250:1da2a24e84]. Người đang bị quản chế hành chính, đang bị truy cứu trách nhiệm hình sự, hoặc đã bị kết án chưa được xóa án tích thì không được làm Hòa giải viên [struct1000:nd99_2011:p13:o26250:1da2a24e84].

> `struct1000:nd99_2011:p13:o26250:1da2a24e84` (trang 13): [Nghị định 99/2011/NĐ-CP · Chương VI · Điều 32]
Điều 32. Hòa giải viên
1. Công dân Việt Nam có đủ các điều kiện sau đây có thể làm Hòa giải viên:
a) Có năng lực hành vi dân sự đầy đủ;
b) Có phẩm chất đạo đức tốt, trung thực;
c) Có ít nhất năm (05) năm kinh nghiệm công tác.
2. Người đang bị quản chế hành chính, đang bị truy cứu trách nhiệm hình sự
hoặc đã bị kết án mà chưa được xóa án tích không được làm Hòa giải viên.

_auto: context có evidence = True, citation chứa evidence = True_

---

## d08 · dieu_kien · có đáp án · status `answered`
**Hỏi:** Khi doanh nghiệp đổi sản phẩm mới cho khách trong quá trình bảo hành thì thời hạn bảo hành của sản phẩm đó được tính từ khi nào?

**Đáp án chuẩn:** Tính (lại) từ thời điểm đổi sản phẩm, hàng hóa mới.
**Gold:** [{'source_id': 'luat19_2023', 'page': 23, 'evidence': 'thời hạn bảo hành sản phẩm, hàng hóa đó được tính lại từ thời điểm đổi mới sản phẩm, hàng hóa'}, {'source_id': 'luat59_2010', 'page': 10, 'evidence': 'được tính từ thời điểm thay thế linh kiện, phụ kiện hoặc đổi hàng hóa mới'}]

- search `thời hạn bảo hành sản phẩm đổi sản phẩm mới trong thời gian bảo hành được tính từ khi nào` → mới: C1, C2, C3
- search `thời hạn bảo hành tính từ thời điểm giao sản phẩm đổi mới` → mới: —

**Agent:** Theo Luật 19/2023/QH15 (hiện hành), khi tổ chức, cá nhân kinh doanh đổi sản phẩm, hàng hóa mới thì thời hạn bảo hành của sản phẩm, hàng hóa đó được tính lại từ thời điểm đổi mới sản phẩm, hàng hóa [struct1000:luat19_2023:p23:o43993:718ebcc363]. Quy định này cũng có trước đó tại Luật 59/2010/QH12 (đã được thay thế), theo đó thời hạn bảo hành được tính từ thời điểm đổi hàng hóa mới [struct1000:luat59_2010:p10:o18922:3a430d202c]. Lưu ý: thời gian thực hiện bảo hành không tính vào thời hạn bảo hành [struct1000:luat19_2023:p23:o43993:718ebcc363]; và đối với linh kiện, phụ kiện được thay thế, thời hạn bảo hành cũng được tính lại từ thời điểm thay thế [struct1000:luat19_2023:p23:o43993:718ebcc363].

> `struct1000:luat19_2023:p23:o43993:718ebcc363` (trang 23): [Luật 19/2023/QH15 · Chương II · Điều 30]
c) Cung cấp cho người tiêu dùng văn bản tiếp nhận bảo hành hoặc hình thức
tiếp nhận bảo hành tương đương khác, trong đó ghi rõ thời gian thực hiện bảo
hành. Thời gian thực hiện bảo hành không tính vào thời hạn bảo hành sản phẩm,
hàng hóa, linh kiện, phụ kiện.
Trường hợp tổ chức, cá nhân kinh doanh thay thế linh kiện, phụ kiện thì thời
hạn bảo hành linh kiện, phụ kiện đó được tính lại từ thời điểm thay thế linh kiện,
phụ kiện.
Trường hợp tổ chức, cá nhân kinh doanh đổi sản phẩm, hàng hóa mới thì thời
hạn bảo hành sản phẩm, hàng hóa đó được tính lại từ t

> `struct1000:luat59_2010:p10:o18922:3a430d202c` (trang 10): [Luật 59/2010/QH12 · Chương II · Điều 21]
Điều 21. Trách nhiệm bảo hành hàng hóa, linh kiện, phụ kiện
Hàng hóa, linh kiện, phụ kiện được bảo hành theo thỏa thuận của các bên hoặc
bắt buộc bảo hành theo quy định của pháp luật. Trường hợp hàng hóa, linh kiện, phụ
kiện được bảo hành, tổ chức, cá nhân kinh doanh hàng hóa có trách nhiệm:
1. Thực hiện đầy đủ nghĩa vụ bảo hành hàng hóa, linh kiện, phụ kiện do mình
cung cấp;
2. Cung cấp cho người tiêu dùng giấy tiếp nhận bảo hành, trong đó ghi rõ thời
gian thực hiện bảo hành. Thời gian thực hiện bảo hành không tính vào thời hạn bảo
hành hàng hóa, linh

_auto: context có evidence = True, citation chứa evidence = True_

---

## d09 · dieu_kien · có đáp án · status `answered`
**Hỏi:** Doanh nghiệp có được miễn bồi thường nếu đã thông tin đầy đủ mà người tiêu dùng vẫn cố ý dùng sản phẩm có khuyết tật gây thiệt hại không?

**Đáp án chuẩn:** Có, nếu doanh nghiệp đã áp dụng đầy đủ biện pháp tại Điều 32 và 33, người tiêu dùng đã tiếp nhận đầy đủ thông tin nhưng vẫn cố ý sử dụng.
**Gold:** [{'source_id': 'luat19_2023', 'page': 27, 'evidence': 'người tiêu dùng đã tiếp nhận đầy đủ thông tin nhưng vẫn cố ý sử dụng sản phẩm, hàng hóa có khuyết tật gây thiệt hại'}]

- search `miễn trách nhiệm bồi thường sản phẩm khuyết tật người tiêu dùng cố ý sử dụng` → mới: C1, C2, C3
- search `đã thông báo đầy đủ về khuyết tật, lỗi do người tiêu dùng gây ra, không bồi thường thiệt hại` → mới: C4

**Agent:** Có, theo Luật 19/2023/QH15 (hiện hành). Doanh nghiệp được miễn trách nhiệm bồi thường thiệt hại do sản phẩm có khuyết tật gây ra khi đồng thời: (i) đã áp dụng đầy đủ các biện pháp quy định tại Điều 32 và Điều 33 của Luật; (ii) người tiêu dùng đã tiếp nhận đầy đủ thông tin; và (iii) người tiêu dùng vẫn cố ý sử dụng sản phẩm có khuyết tật gây thiệt hại [struct1000:luat19_2023:p27:o52148:a741b896ef]. Ngoài ra, doanh nghiệp cũng được miễn nếu chứng minh được khuyết tật không thể phát hiện được với trình độ khoa học, công nghệ của thế giới tại thời điểm sản phẩm gây thiệt hại [struct1000:luat19_2023:p27:o52148:a741b896ef]. Nguyên tắc chung là doanh nghiệp có trách nhiệm bồi thường khi sản phẩm có khuyết tật gây thiệt hại đến tính mạng, sức khỏe, tài sản của người tiêu dùng, kể cả khi không biết hoặc không có lỗi [struct1000:luat19_2023:p26:o50458:e3d6b74804].
Lưu ý: Luật 59/2010/QH12 (đã hết hiệu lực) không có trường hợp miễn trách nhiệm do người tiêu dùng cố ý sử dụng; khi đó chỉ được miễn nếu khuyết tật không thể phát hiện với trình độ khoa học, kỹ thuật tại thời điểm cung cấp hàng hóa [struct1000:luat59_2010:p12:o23098:d7ebcf0af8]. Trường hợp cụ thể cần đánh giá theo quy định hiện hành.

> `struct1000:luat19_2023:p27:o52148:a741b896ef` (trang 27): [Luật 19/2023/QH15 · Chương II · Điều 35]
Điều 35. Miễn trách nhiệm bồi thường thiệt hại do sản phẩm, hàng hóa có
khuyết tật gây ra
Tổ chức, cá nhân kinh doanh quy định tại Điều 34 của Luật này được miễn
trách nhiệm bồi thường thiệt hại trong các trường hợp sau đây:
1. Khi chứng minh được khuyết tật của sản phẩm, hàng hóa không thể phát
hiện được với trình độ khoa học, công nghệ của thế giới tính đến thời điểm sản
phẩm, hàng hóa gây thiệt hại;
2. Tổ chức, cá nhân kinh doanh đã áp dụng đầy đủ các biện pháp quy định tại
Điều 32 và Điều 33 của Luật này, người tiêu dùng đã tiếp nhận đầy đủ thông t

> `struct1000:luat19_2023:p26:o50458:e3d6b74804` (trang 26): [Luật 19/2023/QH15 · Chương II · Điều 34]
Điều 34. Bồi thường thiệt hại do sản phẩm, hàng hóa có khuyết tật gây ra
1. Tổ chức, cá nhân kinh doanh có trách nhiệm bồi thường thiệt hại trong
trường hợp sản phẩm, hàng hóa có khuyết tật do mình cung cấp gây thiệt hại đến
tính mạng, sức khỏe, tài sản của người tiêu dùng, kể cả khi tổ chức, cá nhân đó
không biết hoặc không có lỗi trong việc phát sinh khuyết tật, trừ trường hợp quy
định tại Điều 35 của Luật này.

> `struct1000:luat59_2010:p12:o23098:d7ebcf0af8` (trang 12): [Luật 59/2010/QH12 · Chương II · Điều 24]
Điều 24. Miễn trách nhiệm bồi thường thiệt hại do hàng hóa có khuyết tật
gây ra
Tổ chức, cá nhân kinh doanh hàng hóa quy định tại Điều 23 của Luật này được
miễn trách nhiệm bồi thường thiệt hại khi chứng minh được khuyết tật của hàng hóa
không thể phát hiện được với trình độ khoa học, kỹ thuật tại thời điểm tổ chức, cá
nhân kinh doanh hàng hóa cung cấp cho người tiêu dùng.

_auto: context có evidence = True, citation chứa evidence = True_

---

## d10 · dien_dat_lai · có đáp án · status `answered`
**Hỏi:** Sản phẩm khuyết tật chỉ có thể gây hư hại tài sản của người tiêu dùng thì được xếp vào nhóm nào?

**Đáp án chuẩn:** Nhóm B.
**Gold:** [{'source_id': 'luat19_2023', 'page': 25, 'evidence': 'Sản phẩm, hàng hóa có khuyết tật nhóm B là sản phẩm, hàng hóa có khả năng gây thiệt hại cho tài sản của người tiêu dùng'}]

- search `sản phẩm khuyết tật gây thiệt hại về tài sản của người tiêu dùng` → mới: C1, C2, C3
- search `phân loại thiệt hại do sản phẩm khuyết tật gây ra: thiệt hại về sức khỏe, tính mạng, tài sản` → mới: —

**Agent:** Sản phẩm, hàng hóa có khuyết tật chỉ có khả năng gây thiệt hại cho tài sản của người tiêu dùng được xếp vào nhóm B (Điều 33 Luật 19/2023/QH15) [struct1000:luat19_2023:p25:o48174:6d057421d8]. Nhóm A là sản phẩm có khả năng gây thiệt hại cho tính mạng, sức khỏe của người tiêu dùng [struct1000:luat19_2023:p25:o48174:6d057421d8]. Sản phẩm có khả năng gây thiệt hại đồng thời cho tính mạng, sức khỏe và tài sản thì áp dụng quy định đối với nhóm A [struct1000:luat19_2023:p25:o48174:6d057421d8]. Về trách nhiệm bồi thường, tổ chức, cá nhân kinh doanh phải bồi thường thiệt hại đến tính mạng, sức khỏe, tài sản của người tiêu dùng do sản phẩm có khuyết tật gây ra, kể cả khi không biết hoặc không có lỗi trong việc phát sinh khuyết tật, trừ trường hợp tại Điều 35 [struct1000:luat19_2023:p26:o50458:e3d6b74804]. Khuyết tật được hiểu là sản phẩm không bảo đảm an toàn, có khả năng gây thiệt hại cho tính mạng, sức khỏe, tài sản của người tiêu dùng [struct1000:luat19_2023:p2:o1991:39d33c8b49].

> `struct1000:luat19_2023:p26:o50458:e3d6b74804` (trang 26): [Luật 19/2023/QH15 · Chương II · Điều 34]
Điều 34. Bồi thường thiệt hại do sản phẩm, hàng hóa có khuyết tật gây ra
1. Tổ chức, cá nhân kinh doanh có trách nhiệm bồi thường thiệt hại trong
trường hợp sản phẩm, hàng hóa có khuyết tật do mình cung cấp gây thiệt hại đến
tính mạng, sức khỏe, tài sản của người tiêu dùng, kể cả khi tổ chức, cá nhân đó
không biết hoặc không có lỗi trong việc phát sinh khuyết tật, trừ trường hợp quy
định tại Điều 35 của Luật này.

> `struct1000:luat19_2023:p2:o1991:39d33c8b49` (trang 2): [Luật 19/2023/QH15 · Chương I · Điều 3]
4. Sản phẩm, hàng hóa có khuyết tật là sản phẩm, hàng hóa không bảo đảm an
toàn cho người tiêu dùng, có khả năng gây thiệt hại cho tính mạng, sức khỏe, tài
sản của người tiêu dùng nhưng chưa phát hiện được khuyết tật tại thời điểm sản
phẩm, hàng hóa được cung cấp cho người tiêu dùng mặc dù sản phẩm, hàng hóa đó
được sản xuất theo đúng tiêu chuẩn, quy chuẩn kỹ thuật hiện hành, bao gồm:
a) Sản phẩm, hàng hóa sản xuất hàng loạt có khuyết tật phát sinh từ thiết kế
kỹ thuật;
b) Sản phẩm, hàng hóa đơn lẻ có khuyết tật phát sinh từ quá trình sản xuất, chế
biến,

> `struct1000:luat19_2023:p25:o48174:6d057421d8` (trang 25): [Luật 19/2023/QH15 · Chương II · Điều 33]
Điều 33. Thu hồi sản phẩm, hàng hóa có khuyết tật
1. Sản phẩm, hàng hóa có khuyết tật bao gồm:
a) Sản phẩm, hàng hóa có khuyết tật nhóm A là sản phẩm, hàng hóa có khả
năng gây thiệt hại cho tính mạng, sức khỏe của người tiêu dùng;
b) Sản phẩm, hàng hóa có khuyết tật nhóm B là sản phẩm, hàng hóa có khả
năng gây thiệt hại cho tài sản của người tiêu dùng;
c) Sản phẩm, hàng hóa có khuyết tật có khả năng gây thiệt hại cho tính mạng,
sức khỏe, tài sản của người tiêu dùng thì áp dụng các quy định đối với sản phẩm,
hàng hóa có khuyết tật nhóm A.

_auto: context có evidence = True, citation chứa evidence = True_

---

## d11 · truc_tiep · có đáp án · status `answered`
**Hỏi:** Cơ quan tiếp nhận đăng ký có bao nhiêu ngày để thẩm định hồ sơ đăng ký hợp đồng theo mẫu, và có được gia hạn không?

**Đáp án chuẩn:** 30 ngày kể từ ngày nhận hồ sơ hợp lệ; có thể gia hạn thêm tối đa không quá 30 ngày trong trường hợp phức tạp.
**Gold:** [{'source_id': 'nd55_2024', 'page': 7, 'evidence': 'tiến hành thẩm định hồ sơ đăng ký trong thời hạn 30 ngày, kể từ ngày nhận được hồ sơ hợp lệ'}]

- search `đăng ký hợp đồng theo mẫu thời hạn thẩm định hồ sơ gia hạn` → mới: C1, C2, C3
- search `cơ quan tiếp nhận đăng ký hợp đồng mẫu thẩm định trong ngày làm việc` → mới: C4, C5

**Agent:** Theo Nghị định 55/2024/NĐ-CP (hiện hành), cơ quan có thẩm quyền tiếp nhận đăng ký thẩm định hồ sơ trong thời hạn 30 ngày, kể từ ngày nhận được hồ sơ hợp lệ [struct1000:nd55_2024:p7:o11015:ff4cd946d6]. Có thể gia hạn thêm tối đa không quá 30 ngày trong trường hợp phức tạp; khi gia hạn, cơ quan phải thông báo kịp thời cho tổ chức, cá nhân kinh doanh về thời gian và lý do gia hạn [struct1000:nd55_2024:p7:o11015:ff4cd946d6]. Trong quá trình thẩm định, cơ quan có quyền yêu cầu tổ chức, cá nhân kinh doanh giải trình các vấn đề liên quan đến nội dung đăng ký [struct1000:nd55_2024:p7:o11015:ff4cd946d6].

Lưu ý: Nghị định 99/2011/NĐ-CP (đã hết hiệu lực từ 01/7/2024) quy định thời hạn khác là chậm nhất 20 ngày làm việc để ra thông báo chấp nhận hoặc văn bản trả lời không chấp nhận [struct1000:nd99_2011:p5:o10210:ca7ed531ed]; văn bản cũ không áp dụng cho việc thẩm định hiện nay.

> `struct1000:nd55_2024:p7:o11015:ff4cd946d6` (trang 7): [Nghị định 55/2024/NĐ-CP · Chương IV · Điều 10]
Điều 10. Thẩm định hồ sơ đăng ký
1. Cơ quan có thẩm quyền tiếp nhận đăng ký tiến hành thẩm định hồ sơ đăng
ký trong thời hạn 30 ngày, kể từ ngày nhận được hồ sơ hợp lệ theo quy định tại
Điều 9 của Nghị định này và có thể được gia hạn thêm tối đa không quá 30 ngày
trong trường hợp phức tạp. Trong trường hợp gia hạn, cơ quan có thẩm quyền tiếp
nhận đăng ký thông báo kịp thời cho tổ chức, cá nhân kinh doanh về thời gian và
lý do gia hạn.
2. Trong quá trình thẩm định hồ sơ đăng ký, cơ quan có thẩm quyền tiếp nhận
đăng ký có quyền yêu cầu tổ chức, cá 

> `struct1000:nd99_2011:p5:o10210:ca7ed531ed` (trang 5,6): [Nghị định 99/2011/NĐ-CP · Chương III · Điều 14]
Điều 14. Hoàn thành việc đăng ký
1. Chậm nhất hai mươi (20) ngày làm việc kể từ ngày nhận được hồ sơ hợp lệ,
cơ quan có thẩm quyền đăng ký có trách nhiệm ra thông báo về việc chấp nhận
đăng ký hợp đồng theo mẫu, điều kiện giao dịch chung và gửi cho tổ chức, cá nhân
kinh doanh. Trong trường hợp không chấp nhận đăng ký hợp đồng theo mẫu, điều
kiện giao dịch chung thì cơ quan nhà nước có thẩm quyền phải gửi văn bản trả lời
cho tổ chức, cá nhân kinh doanh trong đó nói rõ lý do không chấp nhận.
2. Sau khi hoàn thành thủ tục đăng ký, hợp đồng theo mẫu

_auto: context có evidence = True, citation chứa evidence = True_

---

## d12 · truc_tiep · có đáp án · status `abstain`
**Hỏi:** Doanh nghiệp bán hàng không tại địa điểm giao dịch thường xuyên phải gửi hồ sơ thông báo cho Ủy ban nhân dân cấp xã trước ít nhất bao lâu?

**Đáp án chuẩn:** Tối thiểu 03 ngày làm việc trước khi thực hiện hoạt động.
**Gold:** [{'source_id': 'nd55_2024', 'page': 19, 'evidence': 'tối thiểu 03 ngày làm việc trước khi thực hiện hoạt động'}]

- search `bán hàng không tại địa điểm giao dịch thường xuyên thông báo Ủy ban nhân dân cấp xã trước ngày` → mới: C1, C2, C3
- search `bán hàng không tại địa điểm giao dịch thường xuyên hồ sơ thông báo` → mới: C4
- search `thông báo bán hàng không tại địa điểm giao dịch thường xuyên trước ít nhất ngày làm việc` → mới: —

**Agent:** Tài liệu được tra cứu không đủ bằng chứng để trả lời câu hỏi về thời hạn tối thiểu (trước ít nhất bao nhiêu ngày) mà doanh nghiệp phải gửi hồ sơ thông báo cho Ủy ban nhân dân cấp xã khi bán hàng không tại địa điểm giao dịch thường xuyên.

_auto: context có evidence = False, citation chứa evidence = False_

---

## d13 · dieu_kien · có đáp án · status `answered`
**Hỏi:** Nếu không xác định được người thụ hưởng, tiền bồi thường trong vụ án vì lợi ích công cộng do tổ chức xã hội hoạt động trong phạm vi một tỉnh khởi kiện sẽ được nộp vào đâu?

**Đáp án chuẩn:** Nộp vào ngân sách địa phương.
**Gold:** [{'source_id': 'nd55_2024', 'page': 20, 'evidence': 'hoạt động trên phạm vi một tỉnh, thành phố trực thuộc Trung ương khởi kiện sẽ nộp vào ngân sách địa phương'}]

- search `tiền bồi thường vụ án lợi ích công cộng không xác định được người thụ hưởng nộp vào ngân sách` → mới: C1, C2, C3
- search `tổ chức xã hội khởi kiện vụ án vì lợi ích công cộng người tiêu dùng bồi thường` → mới: C4

**Agent:** Theo Nghị định 55/2024/NĐ-CP (hiện hành), nếu không xác định được đối tượng thụ hưởng, tiền bồi thường thiệt hại trong vụ án do tổ chức xã hội khởi kiện vì lợi ích công cộng của tổ chức hoạt động trên phạm vi một tỉnh, thành phố trực thuộc Trung ương sẽ được nộp vào ngân sách địa phương [struct1000:nd55_2024:p19:o36432:6293df2f55]. (Nếu tổ chức hoạt động trên phạm vi từ hai tỉnh, thành phố trở lên thì nộp vào ngân sách trung ương [struct1000:nd55_2024:p19:o36432:6293df2f55].)

Căn cứ luật: Luật 19/2023/QH15 quy định trong trường hợp không xác định được đối tượng thụ hưởng, số tiền này được sử dụng để phục vụ các hoạt động chung vì quyền lợi người tiêu dùng theo quy định của Chính phủ [struct1000:luat19_2023:p49:o93179:f9cfa7804d]. Nghị định 55/2024 là văn bản quy định cụ thể việc nộp tiền này vào ngân sách như trên [struct1000:nd55_2024:p19:o36432:6293df2f55].

Lưu ý: Nghị định 99/2011/NĐ-CP đã hết hiệu lực từ 01/7/2024 nên không áp dụng. Tài liệu không nêu chi tiết về thủ tục nộp tiền.

> `struct1000:nd55_2024:p19:o36432:6293df2f55` (trang 19,20): [Nghị định 55/2024/NĐ-CP · Chương VII · Điều 28]
Chương VII
BỒI THƯỜNG THIỆT HẠI TRONG VỤ ÁN DÂN SỰ VỀ BẢO VỆ
QUYỀN LỢI NGƯỜI TIÊU DÙNG DO TỔ CHỨC XÃ HỘI
KHỞI KIỆN VÌ LỢI ÍCH CÔNG CỘNG
Điều 28. Tiền bồi thường thiệt hại trong vụ án dân sự về bảo vệ quyền lợi
người tiêu dùng do tổ chức xã hội khởi kiện vì lợi ích công cộng
Trường hợp không xác định được đối tượng thụ hưởng, tiền bồi thường thiệt
hại trong vụ án dân sự về bảo vệ quyền lợi người tiêu dùng do tổ chức xã hội khởi
kiện vì lợi ích công cộng sẽ được nộp vào ngân sách nhà nước theo nguyên tắc sau:
1. Tiền bồi thường thiệt hại của vụ án

> `struct1000:luat19_2023:p49:o93179:f9cfa7804d` (trang 49): [Luật 19/2023/QH15 · Chương V · Điều 73]
Điều 73. Tiền bồi thường thiệt hại trong vụ án dân sự về bảo vệ quyền lợi
người tiêu dùng vì lợi ích công cộng do tổ chức xã hội tham gia bảo vệ quyền
lợi người tiêu dùng khởi kiện
1. Tiền bồi thường thiệt hại và đối tượng thụ hưởng trong vụ án dân sự về bảo
vệ quyền lợi người tiêu dùng vì lợi ích công cộng do tổ chức xã hội tham gia bảo
vệ quyền lợi người tiêu dùng khởi kiện được thực hiện theo bản án, quyết định của
Tòa án.
2. Trong trường hợp không xác định được đối tượng thụ hưởng, tiền bồi
thường thiệt hại trong vụ án dân sự về bảo vệ quyền lợi ngư

_auto: context có evidence = True, citation chứa evidence = True_

---

## d14 · truc_tiep · có đáp án · status `answered`
**Hỏi:** Luật Bảo vệ quyền lợi người tiêu dùng năm 2010 bắt đầu có hiệu lực thi hành từ ngày nào?

**Đáp án chuẩn:** Từ ngày 01 tháng 7 năm 2011.
**Gold:** [{'source_id': 'luat59_2010', 'page': 20, 'evidence': 'Luật này có hiệu lực thi hành từ ngày 01 tháng 7 năm 2011.'}]

- search `Luật Bảo vệ quyền lợi người tiêu dùng 2010 hiệu lực thi hành từ ngày nào` → mới: C1, C2, C3

**Agent:** Luật Bảo vệ quyền lợi người tiêu dùng số 59/2010/QH12 có hiệu lực thi hành từ ngày 01 tháng 7 năm 2011 [struct1000:luat59_2010:p20:o36605:a486b6cb3f]. Luật này được thay thế bởi Luật 19/2023/QH15 có hiệu lực từ ngày 01 tháng 7 năm 2024, và Luật 59/2010/QH12 hết hiệu lực kể từ ngày đó [struct1000:luat19_2023:p53:o101710:76934ebe4e].

> `struct1000:luat59_2010:p20:o36605:a486b6cb3f` (trang 20): [Luật 59/2010/QH12 · Chương VI · Điều 50]
Chương VI
ĐIỀU KHOẢN THI HÀNH
Điều 50. Hiệu lực thi hành
Luật này có hiệu lực thi hành từ ngày 01 tháng 7 năm 2011.
Pháp lệnh bảo vệ quyền lợi người tiêu dùng số 13/1999/PL-UBTVQH10 hết
hiệu lực kể từ ngày Luật này có hiệu lực.

> `struct1000:luat19_2023:p53:o101710:76934ebe4e` (trang 53): [Luật 19/2023/QH15 · Chương VII · Điều 79]
Điều 79. Hiệu lực thi hành
1. Luật này có hiệu lực thi hành từ ngày 01 tháng 7 năm 2024.
2. Luật Bảo vệ quyền lợi người tiêu dùng số 59/2010/QH12 đã được sửa
đổi, bổ sung một số điều theo Luật số 35/2018/QH14 hết hiệu lực kể từ ngày
Luật này có hiệu lực thi hành, trừ trường hợp quy định tại điểm a khoản 1 và
khoản 2 Điều 80 của Luật này.

_auto: context có evidence = True, citation chứa evidence = True_

---

## d15 · truc_tiep · có đáp án · status `answered`
**Hỏi:** Biên bản hòa giải tranh chấp tiêu dùng theo Luật 2010 phải có chữ ký của những ai?

**Đáp án chuẩn:** Chữ ký của các bên tham gia hòa giải và chữ ký xác nhận của tổ chức, cá nhân tiến hành hòa giải.
**Gold:** [{'source_id': 'luat59_2010', 'page': 16, 'evidence': 'Biên bản hòa giải phải có chữ ký của các bên tham gia hòa giải và chữ ký xác nhận của tổ chức, cá nhân tiến hành hòa giải.'}]

- search `biên bản hòa giải tranh chấp tiêu dùng chữ ký` → mới: C1, C2, C3
- search `hòa giải viên người tiêu dùng tổ chức biên bản hòa giải thành có chữ ký các bên` → mới: C4, C5, C6

**Agent:** Theo Luật 59/2010/QH12 (Điều 36 khoản 2), biên bản hòa giải phải có chữ ký của các bên tham gia hòa giải và chữ ký xác nhận của tổ chức, cá nhân tiến hành hòa giải [struct1000:luat59_2010:p16:o29636:728a4a2c0c].

Biên bản này cũng phải có các nội dung chính: tổ chức, cá nhân tiến hành hòa giải; các bên tham gia; nội dung; thời gian, địa điểm; ý kiến của các bên; kết quả hòa giải; và thời hạn thực hiện kết quả hòa giải thành [struct1000:luat59_2010:p16:o29636:728a4a2c0c].

Lưu ý: Luật 19/2023/QH15 (hiện hành) quy định khác: văn bản về kết quả hòa giải phải có chữ ký hoặc điểm chỉ của các bên, chữ ký xác nhận của cá nhân tiến hành hòa giải và đóng dấu xác nhận của tổ chức tiến hành hòa giải (nếu có) [struct1000:luat19_2023:p46:o88486:d77a32a8a5].

> `struct1000:luat59_2010:p16:o29636:728a4a2c0c` (trang 16): [Luật 59/2010/QH12 · Chương IV · Điều 36]
Điều 36. Biên bản hòa giải
1. Biên bản hòa giải phải có các nội dung chính sau đây:
a) Tổ chức, cá nhân tiến hành hòa giải;
b) Các bên tham gia hòa giải;
c) Nội dung hòa giải;
d) Thời gian, địa điểm tiến hành hòa giải;
đ) Ý kiến của các bên tham gia hòa giải;
e) Kết quả hòa giải;
g) Thời hạn thực hiện kết quả hòa giải thành.
2. Biên bản hòa giải phải có chữ ký của các bên tham gia hòa giải và chữ ký xác
nhận của tổ chức, cá nhân tiến hành hòa giải.

> `struct1000:luat19_2023:p46:o88486:d77a32a8a5` (trang 46,47): [Luật 19/2023/QH15 · Chương V · Điều 65]
Điều 65. Kết quả hòa giải
1. Khi đạt được kết quả hòa giải thành, các bên lập văn bản về kết quả hòa
giải thành.
2. Văn bản về kết quả hòa giải thành đối với trường hợp quy định tại điểm a và
điểm c khoản 1 Điều 63 của Luật này phải có các nội dung sau đây:
a) Tổ chức, cá nhân tiến hành hòa giải;
b) Các bên tham gia hòa giải;
c) Thời gian, địa điểm tiến hành hòa giải;
d) Nội dung hòa giải;
đ) Ý kiến của các bên tham gia hòa giải;
e) Kết quả hòa giải và giải pháp thực hiện;
g) Thời hạn thực hiện kết quả hòa giải thành;
h) Nội dung khác theo thỏa thuận củ

_auto: context có evidence = True, citation chứa evidence = True_

---

## d16 · metadata_filter · có đáp án · status `answered`
**Hỏi:** Theo quy định trước năm 2024, nếu yêu cầu bảo vệ quyền lợi người tiêu dùng gửi cơ quan nhà nước còn thiếu nội dung thì người tiêu dùng phải bổ sung trong bao lâu?

**Đáp án chuẩn:** Trong thời hạn năm (05) ngày làm việc kể từ ngày nhận được yêu cầu bổ sung của cơ quan có thẩm quyền.
**Gold:** [{'source_id': 'nd99_2011', 'page': 9, 'evidence': 'Việc bổ sung phải được thực hiện trong thời hạn năm (05) ngày làm việc kể từ ngày nhận được yêu cầu của cơ quan có thẩm quyền.'}]

- search `yêu cầu bảo vệ quyền lợi người tiêu dùng thiếu nội dung bổ sung trong thời hạn` → mới: C1, C2, C3
- search `Luật bảo vệ quyền lợi người tiêu dùng 2010 yêu cầu gửi cơ quan nhà nước không đầy đủ nội dung bổ sung` → mới: C4

**Agent:** Theo Nghị định 99/2011/NĐ-CP (chế độ 2010), nếu yêu cầu bảo vệ quyền lợi người tiêu dùng thiếu các nội dung quy định tại Điều 20, cơ quan có thẩm quyền yêu cầu người tiêu dùng hoặc tổ chức xã hội bổ sung, và việc bổ sung phải được thực hiện trong thời hạn 05 ngày làm việc kể từ ngày nhận được yêu cầu của cơ quan có thẩm quyền [struct1000:nd99_2011:p9:o19006:a4b10855a6]. Các nội dung bắt buộc của yêu cầu gồm: thông tin về tổ chức, cá nhân kinh doanh vi phạm; thông tin về tổ chức xã hội hoặc người tiêu dùng yêu cầu; nội dung vụ việc; yêu cầu cụ thể; và tài liệu, chứng cứ kèm theo [struct1000:nd99_2011:p9:o18244:7a5cc2ba37].

> `struct1000:nd99_2011:p9:o19006:a4b10855a6` (trang 9): [Nghị định 99/2011/NĐ-CP · Chương IV · Điều 21]
Điều 21. Thủ tục tiếp nhận yêu cầu
1. Trường hợp yêu cầu bảo vệ quyền lợi người tiêu dùng được lập bằng văn
bản, cán bộ phụ trách tiếp nhận có trách nhiệm xem xét và tiếp nhận yêu cầu.
Trường hợp yêu cầu bảo vệ quyền lợi người tiêu dùng được trình bày trực tiếp,
cán bộ phụ trách tiếp nhận phải lập thành văn bản và yêu cầu người tiêu dùng hoặc
người đại diện của tổ chức xã hội tham gia bảo vệ quyền lợi người tiêu dùng ký tên
hoặc điểm chỉ xác nhận vào văn bản đó.
2. Trường hợp yêu cầu bảo vệ quyền lợi người tiêu dùng thiếu các nội dung
quy định tạ

> `struct1000:nd99_2011:p9:o18244:7a5cc2ba37` (trang 9): [Nghị định 99/2011/NĐ-CP · Chương IV · Điều 20]
Chương IV
GIẢI QUYẾT YÊU CẦU BẢO VỆ QUYỀN LỢI NGƯỜI TIÊU DÙNG
Điều 20. Hình thức, nội dung của yêu cầu bảo vệ quyền lợi người tiêu dùng
1. Người tiêu dùng, tổ chức xã hội tham gia bảo vệ quyền lợi người tiêu dùng
có quyền yêu cầu cơ quan quản lý nhà nước về bảo vệ quyền lợi người tiêu dùng
theo quy định tại Điều 25 Luật Bảo vệ quyền lợi người tiêu dùng. Việc yêu cầu có
thể được thực hiện bằng văn bản hoặc yêu cầu trực tiếp.
2. Yêu cầu bảo vệ quyền lợi người tiêu dùng phải có các nội dung sau:
a) Thông tin về tổ chức, cá nhân kinh doanh vi phạm;
b

_auto: context có evidence = True, citation chứa evidence = True_

---

## d17 · ngoai_le · có đáp án · status `answered`
**Hỏi:** Cơ quan quản lý nhà nước có tiếp nhận yêu cầu hỗ trợ thương lượng nếu người gửi yêu cầu không phải là người tiêu dùng không?

**Đáp án chuẩn:** Không; đây là một trường hợp không tiếp nhận và giải quyết yêu cầu hỗ trợ thương lượng (trừ khi là người đại diện hợp pháp của người tiêu dùng).
**Gold:** [{'source_id': 'luat19_2023', 'page': 43, 'evidence': 'Người yêu cầu hỗ trợ thương lượng không phải là người tiêu dùng hoặc người đại diện hợp pháp của người tiêu dùng.'}]

- search `hỗ trợ người tiêu dùng thương lượng yêu cầu tổ chức xã hội tiếp nhận yêu cầu` → mới: C1, C2, C3
- search `cơ quan nhà nước hỗ trợ thương lượng người tiêu dùng điều kiện tiếp nhận yêu cầu` → mới: C4

**Agent:** Không. Theo Luật 19/2023/QH15 (Điều 58, khoản 2), cơ quan quản lý nhà nước và tổ chức xã hội không tiếp nhận và giải quyết yêu cầu hỗ trợ thương lượng nếu người yêu cầu không phải là người tiêu dùng hoặc người đại diện hợp pháp của người tiêu dùng [struct1000:luat19_2023:p43:o83500:77d12f7b8e]. Lưu ý: quyền yêu cầu hỗ trợ thương lượng phát sinh khi người tiêu dùng bị tổ chức, cá nhân kinh doanh không trả lời hoặc từ chối thương lượng mà không có lý do chính đáng, và quyền, lợi ích hợp pháp của họ bị xâm phạm [struct1000:luat19_2023:p42:o81059:c6b7a6e583]. Ngoài ra, yêu cầu còn có thể không được tiếp nhận trong các trường hợp khác tại Điều 58 (ví dụ: người tiêu dùng không đủ thông tin xác định tổ chức, cá nhân liên quan; nội dung không thuộc thẩm quyền; yêu cầu đã được giải quyết trước đó) [struct1000:luat19_2023:p43:o83500:77d12f7b8e].

> `struct1000:luat19_2023:p43:o83500:77d12f7b8e` (trang 43,44): [Luật 19/2023/QH15 · Chương V · Điều 58]
Điều 58. Trường hợp không tiếp nhận và giải quyết yêu cầu hỗ trợ
thương lượng
1. Người tiêu dùng là người chưa thành niên, người mất năng lực hành vi dân
sự hoặc hạn chế năng lực hành vi dân sự hoặc có khó khăn trong nhận thức, làm
chủ hành vi mà không có người đại diện hợp pháp.
2. Người yêu cầu hỗ trợ thương lượng không phải là người tiêu dùng hoặc
người đại diện hợp pháp của người tiêu dùng.
3. Người tiêu dùng không cung cấp đầy đủ thông tin, tài liệu để xác định chính
xác tổ chức, cá nhân có liên quan hoặc bằng chứng liên quan đến giao dịch.
4. Nội 

> `struct1000:luat19_2023:p42:o81059:c6b7a6e583` (trang 42): [Luật 19/2023/QH15 · Chương V · Điều 56]
Mục 2
THƯƠNG LƯỢNG
Điều 56. Yêu cầu và tiếp nhận thương lượng
1. Người tiêu dùng có quyền yêu cầu tổ chức, cá nhân kinh doanh thương lượng.
2. Tổ chức, cá nhân kinh doanh phải tiếp nhận yêu cầu thương lượng của người
tiêu dùng theo quy định tại Điều 57 của Luật này.
3. Trường hợp tổ chức, cá nhân kinh doanh không trả lời yêu cầu thương lượng
của người tiêu dùng theo quy định tại Điều 57 của Luật này hoặc từ chối thương
lượng mà không có lý do chính đáng, người tiêu dùng có quyền yêu cầu cơ quan
quản lý nhà nước về bảo vệ quyền lợi người tiêu dùng, tổ ch

_auto: context có evidence = True, citation chứa evidence = True_

---

## d18 · dien_dat_lai · có đáp án · status `answered`
**Hỏi:** Ban quản lý chợ phải bố trí thiết bị gì để khách hàng tự kiểm tra khối lượng hàng hóa đã mua?

**Đáp án chuẩn:** Đặt và duy trì hoạt động của cân đối chứng, thiết bị đo lường tại chợ, trung tâm thương mại.
**Gold:** [{'source_id': 'nd55_2024', 'page': 4, 'evidence': 'Đặt và duy trì hoạt động của cân đối chứng, thiết bị đo lường tại các chợ, trung tâm thương mại'}, {'source_id': 'nd99_2011', 'page': 3, 'evidence': 'Đặt và duy trì hoạt động của cân đối chứng, thiết bị đo lường tại các chợ, trung tâm thương mại'}]

- search `ban quản lý chợ bố trí thiết bị khách hàng tự kiểm tra khối lượng hàng hóa` → mới: C1, C2, C3
- search `chợ phải có cân đối chứng để người tiêu dùng kiểm tra lại khối lượng` → mới: C4

**Agent:** Ban quản lý chợ phải đặt và duy trì hoạt động của cân đối chứng, thiết bị đo lường tại chợ để người tiêu dùng tự kiểm tra về số lượng, khối lượng hàng hóa [struct1000:nd55_2024:p4:o5678:237102acac]. Cân đối chứng, thiết bị đo lường này phải được kiểm định và còn trong thời hạn kiểm định theo quy định của pháp luật về đo lường [struct1000:nd55_2024:p4:o5678:237102acac]. Quy định tương tự đã có trong Nghị định 99/2011/NĐ-CP (đã hết hiệu lực từ 01/7/2024) [struct1000:nd99_2011:p2:o3495:14baf53701].

> `struct1000:nd55_2024:p4:o5678:237102acac` (trang 4): [Nghị định 55/2024/NĐ-CP · Chương III · Điều 5]
Điều 5. Trách nhiệm của tổ chức quản lý chợ, trung tâm thương mại
1. Ban hành nội quy theo quy định của pháp luật trong đó phải có các nội dung
cơ bản về bảo vệ quyền lợi người tiêu dùng, bao gồm: quyền và trách nhiệm của
người tiêu dùng, người bán hàng; người có trách nhiệm tiếp nhận, giải quyết yêu
cầu, phản ánh của người tiêu dùng và biện pháp xử lý vi phạm.
2. Hòa giải tranh chấp giữa người tiêu dùng và người bán hàng trong phạm vi
chợ, trung tâm thương mại khi được yêu cầu.
3. Đặt và duy trì hoạt động của cân đối chứng, thiết bị đo lường tại

> `struct1000:nd99_2011:p2:o3495:14baf53701` (trang 2,3): [Nghị định 99/2011/NĐ-CP · Chương II · Điều 5]
Điều 5. Trách nhiệm của Ban quản lý chợ, thương nhân kinh doanh chợ,
trung tâm thương mại
1. Ban hành nội quy theo quy định của pháp luật trong đó phải có các nội dung
cơ bản về bảo vệ quyền lợi người tiêu dùng, bao gồm:
a) Quyền và trách nhiệm của người tiêu dùng;
b) Quyền và trách nhiệm của người bán hàng;
c) Người có trách nhiệm tiếp nhận, giải quyết yêu cầu, phản ánh của người tiêu
dùng;
d) Biện pháp xử lý vi phạm.
2. Hòa giải tranh chấp giữa người tiêu dùng và người bán hàng trong phạm vi
chợ, trung tâm thương mại khi được yêu cầu.
3. Đặt và 

_auto: context có evidence = True, citation chứa evidence = True_

---

## u01 · thieu_bang_chung · THIẾU BẰNG CHỨNG · status `abstain`
**Hỏi:** Mức phạt tiền tối đa đối với tổ chức kinh doanh vi phạm pháp luật về bảo vệ quyền lợi người tiêu dùng là bao nhiêu đồng?

**Lý do thiếu:** Corpus chỉ nói tổ chức vi phạm 'bị xử phạt vi phạm hành chính' và 'Chính phủ quy định chi tiết việc xử phạt' (Luật 59/2010 Điều 11, trang 6); mức phạt nằm ở nghị định xử phạt riêng, không có trong 4 văn bản.

- search `mức phạt tiền tối đa đối với tổ chức kinh doanh vi phạm pháp luật bảo vệ quyền lợi người tiêu dùng` → mới: C1, C2, C3
- search `xử phạt vi phạm hành chính trong lĩnh vực bảo vệ quyền lợi người tiêu dùng mức phạt tiền đối với tổ chức` → mới: C4, C5
- search `Nghị định 55/2024 phạt tiền đối với tổ chức vi phạm quy định về bảo vệ người tiêu dùng mức phạt tối đa đồng` → mới: C6, C7

**Agent:** Tài liệu hiện có không đủ bằng chứng để xác định mức phạt tiền tối đa đối với tổ chức kinh doanh vi phạm pháp luật về bảo vệ quyền lợi người tiêu dùng. Các đoạn tìm được chỉ quy định chung rằng tổ chức vi phạm bị xử phạt vi phạm hành chính tùy tính chất, mức độ vi phạm, và Chính phủ quy định chi tiết việc xử phạt; không có đoạn nào nêu con số mức phạt tiền tối đa. Đề nghị tra cứu trực tiếp Nghị định 55/2024/NĐ-CP (chế độ hiện hành) hoặc văn bản xử phạt vi phạm hành chính liên quan để có con số chính xác.


---

## u02 · thieu_bang_chung · THIẾU BẰNG CHỨNG · status `abstain`
**Hỏi:** Thời hiệu khởi kiện vụ án dân sự về bảo vệ quyền lợi người tiêu dùng là bao nhiêu năm?

**Lý do thiếu:** Corpus quy định ai được khởi kiện, điều kiện và thủ tục rút gọn nhưng không quy định thời hiệu khởi kiện (thuộc Bộ luật Dân sự / Tố tụng dân sự).

- search `thời hiệu khởi kiện vụ án dân sự bảo vệ quyền lợi người tiêu dùng` → mới: C1, C2, C3
- search `thời hiệu yêu cầu bảo vệ quyền lợi người tiêu dùng năm năm` → mới: C4, C5, C6
- search `thời hiệu khởi kiện quyền yêu cầu người tiêu dùng bồi thường thiệt hại` → mới: C7, C8

**Agent:** Tài liệu được cung cấp không đủ bằng chứng để trả lời. Các đoạn tìm được (Luật 59/2010/QH12, Luật 19/2023/QH15 và Nghị định 55/2024/NĐ-CP) quy định về vụ án dân sự bảo vệ quyền lợi người tiêu dùng, điều kiện khởi kiện của tổ chức xã hội, công khai thông báo thụ lý và tiền bồi thường thiệt hại, nhưng không quy định thời hiệu khởi kiện bằng số năm. Thời hiệu khởi kiện thường được quy định trong pháp luật tố tụng dân sự, không có trong kho tài liệu hiện tại.


---

## u03 · thieu_bang_chung · THIẾU BẰNG CHỨNG · status `abstain`
**Hỏi:** Khi hãng hàng không hủy chuyến bay, người tiêu dùng được hoàn lại bao nhiêu phần trăm giá vé?

**Lý do thiếu:** Không có quy định về vận tải hàng không, vé hay tỷ lệ hoàn tiền. Cụm 'hàng không' trong corpus chỉ xuất hiện trong 'bán hàng không tại địa điểm giao dịch thường xuyên' (bẫy lexical).

- search `hãng hàng không hủy chuyến bay hoàn lại giá vé tỷ lệ phần trăm` → mới: C1, C2, C3
- search `hủy chuyến bay người tiêu dùng được hoàn tiền vé máy bay` → mới: C4
- search `vận chuyển hàng không chuyến bay bị hủy hoàn trả 100% giá vé` → mới: C5

**Agent:** Tài liệu trong kho không đủ bằng chứng để trả lời. Các đoạn tìm được (Luật 19/2023/QH15, Luật 59/2010/QH12, Nghị định 99/2011/NĐ-CP) chỉ quy định chung về việc hoàn trả tiền khi người tiêu dùng đơn phương chấm dứt hợp đồng (trong 30 ngày), không đề cập đến trường hợp hãng hàng không hủy chuyến bay hay tỷ lệ phần trăm giá vé được hoàn lại.


---
