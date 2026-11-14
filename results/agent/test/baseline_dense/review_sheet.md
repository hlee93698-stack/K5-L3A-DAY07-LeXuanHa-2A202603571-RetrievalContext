# Review sheet — test / baseline_dense

Model claude-haiku-5-5, method dense, top-k 3, budget 6000 ký tự, max_searches 3, neighbors False, prompt v1, effort medium.

## t01 · metadata_filter · có đáp án · status `answered`
**Hỏi:** Theo quy định hiện hành, hòa giải viên thuộc tổ chức hòa giải tranh chấp tiêu dùng cần có kỹ năng và hiểu biết gì?

**Đáp án chuẩn:** Có kỹ năng hòa giải, hiểu biết pháp luật về bảo vệ quyền lợi người tiêu dùng và pháp luật khác có liên quan.
**Gold:** [{'source_id': 'luat19_2023', 'page': 46, 'evidence': 'Có kỹ năng hòa giải, hiểu biết pháp luật về bảo vệ quyền lợi người tiêu dùng và pháp luật khác có liên quan'}]

- search `tiêu chuẩn hòa giải viên tranh chấp tiêu dùng kỹ năng hiểu biết` → mới: C1, C2, C3

**Agent:** Theo Điều 64 Luật 19/2023/QH15, hòa giải viên thuộc tổ chức hòa giải quy định tại điểm a và điểm c khoản 1 Điều 63 (tổ chức xã hội tham gia bảo vệ quyền lợi người tiêu dùng; tổ chức khác có chức năng hòa giải theo quy định) phải là công dân Việt Nam và đáp ứng đủ các điều kiện sau:
- Có năng lực hành vi dân sự đầy đủ [struct1000:luat19_2023:p46:o87407:a734a81d41];
- Có phẩm chất đạo đức tốt, trung thực, có uy tín [struct1000:luat19_2023:p46:o87407:a734a81d41];
- Có kỹ năng hòa giải và hiểu biết pháp luật về bảo vệ quyền lợi người tiêu dùng và pháp luật khác có liên quan [struct1000:luat19_2023:p46:o87407:a734a81d41];
- Không đang trong thời gian bị truy cứu trách nhiệm hình sự hoặc đã bị kết án mà chưa được xóa án tích [struct1000:luat19_2023:p46:o87407:a734a81d41].
Tổ chức hòa giải này có trách nhiệm công nhận, công bố Danh sách hòa giải viên đủ điều kiện và chỉ định hòa giải viên theo yêu cầu của các bên [struct1000:luat19_2023:p45:o86700:780a5f6dc9].
Ngoài ra, hòa giải viên theo pháp luật về hòa giải có liên quan cũng là một nhóm hòa giải viên được quy định riêng [struct1000:luat19_2023:p46:o87407:a734a81d41].

> `struct1000:luat19_2023:p46:o87407:a734a81d41` (trang 46): [Luật 19/2023/QH15 · Chương V · Điều 64]
Điều 64. Hòa giải viên
Hòa giải viên hòa giải tranh chấp giữa người tiêu dùng và tổ chức, cá nhân
kinh doanh bao gồm:
1. Hòa giải viên theo quy định của pháp luật về hòa giải có liên quan;
2. Hòa giải viên thuộc tổ chức quy định tại điểm a và điểm c khoản 1 Điều 63
của Luật này là công dân Việt Nam đáp ứng đủ các điều kiện sau đây:
a) Có năng lực hành vi dân sự đầy đủ;
b) Có phẩm chất đạo đức tốt, trung thực, có uy tín;
c) Có kỹ năng hòa giải, hiểu biết pháp luật về bảo vệ quyền lợi người tiêu dùng
và pháp luật khác có liên quan;
d) Không đang trong thờ

> `struct1000:luat19_2023:p45:o86700:780a5f6dc9` (trang 45): [Luật 19/2023/QH15 · Chương V · Điều 63]
Điều 63. Tổ chức hòa giải
1. Tổ chức hòa giải tranh chấp giữa người tiêu dùng và tổ chức, cá nhân kinh
doanh bao gồm:
a) Tổ chức xã hội tham gia bảo vệ quyền lợi người tiêu dùng;
b) Tổ chức hòa giải theo quy định của pháp luật về hòa giải thương mại, pháp
luật về hòa giải tại cơ sở, pháp luật về hòa giải tại tòa án;
c) Tổ chức khác có chức năng hòa giải tranh chấp giữa người tiêu dùng và tổ
chức, cá nhân kinh doanh theo quy định của pháp luật.
2. Tổ chức hòa giải theo quy định tại điểm a và điểm c khoản 1 Điều này có
trách nhiệm công nhận, công bố Danh 

_auto: context có evidence = True, citation chứa evidence = True_

---

## t02 · metadata_filter · có đáp án · status `answered`
**Hỏi:** Với hàng hóa bán năm 2015 (áp dụng luật cũ), khi phát hiện khuyết tật, nhà sản xuất phải thông báo công khai việc thu hồi trên báo hoặc đài như thế nào?

**Đáp án chuẩn:** Ít nhất 05 số liên tiếp trên báo ngày hoặc 05 ngày liên tiếp trên đài phát thanh, truyền hình tại địa phương nơi hàng hóa lưu thông.
**Gold:** [{'source_id': 'luat59_2010', 'page': 11, 'evidence': 'ít nhất 05 số liên tiếp trên báo ngày hoặc 05 ngày liên tiếp trên đài phát thanh, truyền hình tại địa phương mà hàng hóa đó được lưu thông'}]

- search `nhà sản xuất thu hồi hàng hóa khuyết tật thông báo công khai trên báo hoặc đài` → mới: C1, C2, C3
- search `thông báo thu hồi hàng hóa có khuyết tật trên báo viết, báo nói, báo hình trung ương hoặc địa phương` → mới: —

**Agent:** Theo Điều 22 Luật 59/2010/QH12, khi phát hiện hàng hóa có khuyết tật, tổ chức, cá nhân sản xuất (và nhập khẩu) phải kịp thời ngừng cung cấp hàng hóa đó ra thị trường [struct1000:luat59_2010:p11:o20713:5dcc945667]. Việc thông báo công khai được thực hiện như sau:
- Thông báo công khai về hàng hóa có khuyết tật và việc thu hồi ít nhất 05 số liên tiếp trên báo ngày, hoặc 05 ngày liên tiếp trên đài phát thanh, truyền hình tại địa phương nơi hàng hóa đó được lưu thông [struct1000:luat59_2010:p11:o20713:5dcc945667].
- Nội dung thông báo phải gồm: (a) mô tả hàng hóa phải thu hồi; (b) lý do thu hồi và cảnh báo nguy cơ thiệt hại do khuyết tật gây ra; (c) thời gian, địa điểm, phương thức thu hồi; (d) thời gian, phương thức khắc phục khuyết tật; (đ) các biện pháp bảo vệ quyền lợi người tiêu dùng trong quá trình thu hồi [struct1000:luat59_2010:p11:o20713:5dcc945667].
- Phải thu hồi đúng nội dung đã thông báo công khai và chịu các chi phí phát sinh trong quá trình thu hồi; sau khi hoàn thành phải báo cáo kết quả cho cơ quan quản lý nhà nước về bảo vệ quyền lợi người tiêu dùng cấp tỉnh nơi thu hồi (nếu thu hồi trên từ hai tỉnh trở lên thì báo cáo cho cơ quan ở trung ương) [struct1000:luat59_2010:p11:o21551:4652bf1c96].
Lưu ý: tài liệu tìm được không nêu chi tiết hơn về cách thức đăng tải (vị trí, kích thước, thời điểm trong ngày) ngoài các yêu cầu trên.

> `struct1000:luat59_2010:p11:o20713:5dcc945667` (trang 11): [Luật 59/2010/QH12 · Chương II · Điều 22]
Điều 22. Trách nhiệm thu hồi hàng hóa có khuyết tật
Khi phát hiện hàng hóa có khuyết tật, tổ chức, cá nhân sản xuất, nhập khẩu hàng
hóa có trách nhiệm:
1. Kịp thời tiến hành mọi biện pháp cần thiết để ngừng việc cung cấp hàng hóa
có khuyết tật trên thị trường;
2. Thông báo công khai về hàng hóa có khuyết tật và việc thu hồi hàng hóa đó ít
nhất 05 số liên tiếp trên báo ngày hoặc 05 ngày liên tiếp trên đài phát thanh, truyền
hình tại địa phương mà hàng hóa đó được lưu thông với các nội dung sau đây:
a) Mô tả hàng hóa phải thu hồi;
b) Lý do thu hồi hàng h

> `struct1000:luat59_2010:p11:o21551:4652bf1c96` (trang 11): [Luật 59/2010/QH12 · Chương II · Điều 22]
3. Thực hiện việc thu hồi hàng hóa có khuyết tật đúng nội dung đã thông báo
công khai và chịu các chi phí phát sinh trong quá trình thu hồi;
4. Báo cáo kết quả cho cơ quan quản lý nhà nước về bảo vệ quyền lợi người tiêu
dùng cấp tỉnh nơi thực hiện thu hồi hàng hóa có khuyết tật sau khi hoàn thành việc
thu hồi; trường hợp việc thu hồi hàng hóa có khuyết tật được tiến hành trên địa bàn
từ hai tỉnh trở lên thì báo cáo kết quả cho cơ quan quản lý nhà nước về bảo vệ quyền
lợi người tiêu dùng ở trung ương.

_auto: context có evidence = True, citation chứa evidence = True_

---

## t03 · ngoai_le · có đáp án · status `answered`
**Hỏi:** Tổ chức xã hội khởi kiện vụ án dân sự vì lợi ích công cộng để bảo vệ người tiêu dùng có phải chịu án phí không?

**Đáp án chuẩn:** Không phải nộp tiền tạm ứng án phí và không phải chịu án phí.
**Gold:** [{'source_id': 'luat19_2023', 'page': 48, 'evidence': 'vì lợi ích công cộng không phải nộp tiền tạm ứng án phí, không phải chịu án phí'}]

- search `tổ chức xã hội khởi kiện vụ án dân sự vì lợi ích công cộng bảo vệ người tiêu dùng án phí` → mới: C1, C2, C3
- search `miễn án phí tổ chức xã hội khởi kiện vì lợi ích công cộng` → mới: C4

**Agent:** Không. Theo Luật 19/2023/QH15 (hiện hành), tổ chức xã hội tham gia bảo vệ quyền lợi người tiêu dùng khởi kiện vụ án dân sự về bảo vệ quyền lợi người tiêu dùng vì lợi ích công cộng không phải nộp tiền tạm ứng án phí và không phải chịu án phí [struct1000:luat19_2023:p48:o91525:df6fcf7de1]. Điều kiện để tổ chức được tự khởi kiện vì lợi ích công cộng theo Luật 2023 gồm: được thành lập hợp pháp; có tôn chỉ, mục đích hoạt động vì quyền lợi người tiêu dùng hoặc vì lợi ích công cộng liên quan; có thời gian hoạt động tối thiểu 01 năm tính đến ngày khởi kiện; và có phạm vi hoạt động từ cấp huyện trở lên [struct1000:luat19_2023:p40:o77136:14e8c73743]. Lưu ý: Nghị định 99/2011/NĐ-CP (đã hết hiệu lực từ 01/7/2024) quy định tổ chức phải chịu các chi phí phát sinh trong quá trình khởi kiện [struct1000:nd99_2011:p11:o23052:276160613a]; quy định này không còn là căn cứ hiện hành, và tài liệu được cung cấp không có điều khoản hiện hành nào về chi phí khác ngoài án phí.

> `struct1000:luat19_2023:p40:o77136:14e8c73743` (trang 40): [Luật 19/2023/QH15 · Chương IV · Điều 50]
2. Tổ chức xã hội tham gia bảo vệ quyền lợi người tiêu dùng có quyền tự mình
khởi kiện vụ án dân sự về bảo vệ quyền lợi người tiêu dùng vì lợi ích công cộng
khi có đủ các điều kiện sau đây:
a) Được thành lập hợp pháp theo quy định của pháp luật;
b) Có tôn chỉ, mục đích hoạt động vì quyền lợi người tiêu dùng hoặc vì lợi ích
công cộng liên quan đến quyền lợi người tiêu dùng;
c) Có thời gian hoạt động tối thiểu 01 năm kể từ ngày tổ chức xã hội được
thành lập đến ngày tổ chức xã hội thực hiện quyền tự khởi kiện;
d) Có phạm vi hoạt động từ cấp huyện trở lên

> `struct1000:nd99_2011:p11:o23052:276160613a` (trang 11): [Nghị định 99/2011/NĐ-CP · Chương V · Điều 25]
Điều 25. Nghĩa vụ của tổ chức xã hội tham gia bảo vệ quyền lợi người tiêu
dùng khi tự mình khởi kiện vụ án bảo vệ người tiêu dùng vì lợi ích công cộng
Khi tự mình khởi kiện vụ án bảo vệ quyền lợi người tiêu dùng vì lợi ích công
cộng, tổ chức xã hội tham gia bảo vệ quyền lợi người tiêu dùng có nghĩa vụ sau:
1. Thông báo thông tin về nội dung vụ án theo quy định tại Điều 44 Luật Bảo
vệ quyền lợi người tiêu dùng.
2. Đảm bảo quyền tham gia vụ án của những người tiêu dùng có liên quan đến
vụ án.
3. Chịu các chi phí phát sinh trong quá trình khởi kiện.

> `struct1000:luat19_2023:p48:o91525:df6fcf7de1` (trang 48): [Luật 19/2023/QH15 · Chương V · Điều 71]
Điều 71. Án phí đối với vụ án dân sự về bảo vệ quyền lợi người tiêu dùng
1. Án phí đối với vụ án dân sự về bảo vệ quyền lợi người tiêu dùng được thực
hiện theo quy định của pháp luật về án phí, lệ phí Tòa án và quy định của Luật này.
2. Người tiêu dùng khởi kiện vụ án dân sự bảo vệ quyền, lợi ích hợp pháp của
mình, tổ chức xã hội tham gia bảo vệ quyền lợi người tiêu dùng đại diện cho người
tiêu dùng theo ủy quyền khởi kiện vụ án dân sự về bảo vệ quyền lợi người tiêu
dùng không phải nộp tiền tạm ứng án phí.
3. Tổ chức xã hội tham gia bảo vệ quyền lợi ngư

_auto: context có evidence = True, citation chứa evidence = True_

---

## t04 · dien_dat_lai · có đáp án · status `answered`
**Hỏi:** Nền tảng số lớn có chức năng tìm kiếm phải công khai điều gì về cách sắp xếp thứ tự hiển thị sản phẩm?

**Đáp án chuẩn:** Công bố công khai tiêu chí xác định ưu tiên hiển thị sản phẩm, hàng hóa, dịch vụ; nội dung có thu phí/được tài trợ phải công khai tại kết quả tìm kiếm.
**Gold:** [{'source_id': 'nd55_2024', 'page': 15, 'evidence': 'Công bố công khai tiêu chí xác định ưu tiên hiển thị sản phẩm, hàng hóa, dịch vụ nếu nền tảng số có chức năng tìm kiếm.'}]

- search `nền tảng số có chức năng tìm kiếm công khai thông tin xếp hạng thứ tự hiển thị kết quả tìm kiếm` → mới: C1, C2, C3
- search `Luật 19/2023 bảo vệ quyền lợi người tiêu dùng nền tảng thương mại điện tử công khai nguyên tắc xếp hạng sản phẩm` → mới: C4, C5, C6

**Agent:** Theo Nghị định 55/2024/NĐ-CP, Điều 23, tổ chức thiết lập, vận hành nền tảng số lớn có chức năng tìm kiếm phải công bố công khai tiêu chí xác định ưu tiên hiển thị sản phẩm, hàng hóa, dịch vụ [struct1000:nd55_2024:p15:o28119:fd491db37d]. Nếu nội dung hiển thị là nội dung có thu phí hoặc được tài trợ thì phải công khai ngay tại kết quả tìm kiếm sản phẩm, hàng hóa, dịch vụ [struct1000:nd55_2024:p15:o28119:fd491db37d]. Việc xây dựng và áp dụng các tiêu chí ưu tiên hiển thị phải tuân thủ pháp luật liên quan [struct1000:nd55_2024:p15:o28119:fd491db37d]. Ngoài ra, Luật 19/2023/QH15, Điều 10 khoản 3b cấm việc hạn chế quyền lựa chọn của người tiêu dùng thông qua sắp xếp ưu tiên sản phẩm giữa các tổ chức, cá nhân kinh doanh mà không công khai tiêu chí lựa chọn [struct1000:luat19_2023:p11:o20451:99c865484a].

> `struct1000:nd55_2024:p15:o28119:fd491db37d` (trang 15): [Nghị định 55/2024/NĐ-CP · Chương VI · Điều 23]
Điều 23. Trách nhiệm của tổ chức thiết lập, vận hành nền tảng số lớn
1. Công bố công khai tiêu chí xác định ưu tiên hiển thị sản phẩm, hàng hóa,
dịch vụ nếu nền tảng số có chức năng tìm kiếm. Trường hợp nội dung hiển thị là
nội dung có thu phí hoặc được tài trợ thì phải công khai tại kết quả tìm kiếm sản
phẩm, hàng hóa, dịch vụ.
Việc xây dựng và công bố áp dụng các tiêu chí để xác định việc ưu tiên hiển
thị sản phẩm, hàng hóa, dịch vụ khi sử dụng chức năng tìm kiếm phải tuân thủ các
quy định của pháp luật có liên quan.

> `struct1000:luat19_2023:p11:o20451:99c865484a` (trang 11): [Luật 19/2023/QH15 · Chương I · Điều 10]
3. Tổ chức, cá nhân kinh doanh thiết lập, vận hành, cung cấp dịch vụ nền tảng
số bị nghiêm cấm thực hiện các hành vi sau đây:
a) Ép buộc hoặc ngăn cản người tiêu dùng đăng ký sử dụng hoặc sử dụng nền
tảng số trung gian khác như là điều kiện bắt buộc để sử dụng dịch vụ;
b) Hạn chế quyền lựa chọn của người tiêu dùng thông qua việc sắp xếp ưu tiên
lựa chọn sản phẩm, hàng hóa, dịch vụ giữa các tổ chức, cá nhân kinh doanh cung
cấp trên nền tảng số mà không công khai tiêu chí lựa chọn;
c) Sử dụng biện pháp ngăn hiển thị hoặc hiển thị không trung thực kết quả


_auto: context có evidence = True, citation chứa evidence = True_

---

## t05 · dieu_kien · có đáp án · status `answered`
**Hỏi:** Theo Nghị định 99/2011, cơ quan có thẩm quyền phải trả lời yêu cầu bảo vệ quyền lợi người tiêu dùng hợp lệ trong bao lâu, và có được gia hạn không?

**Đáp án chuẩn:** 15 ngày làm việc kể từ ngày tiếp nhận yêu cầu hợp lệ; vụ việc phức tạp có thể gia hạn nhưng không quá 15 ngày làm việc.
**Gold:** [{'source_id': 'nd99_2011', 'page': 10, 'evidence': ['Trong thời hạn mười lăm (15) ngày làm việc kể từ ngày tiếp nhận yêu cầu bảo vệ quyền lợi người tiêu dùng hợp lệ', 'thời hạn trả lời có thể được gia hạn nhưng không quá mười lăm (15) ngày làm việc']}]

- search `Nghị định 99/2011 thời hạn trả lời yêu cầu bảo vệ quyền lợi người tiêu dùng hợp lệ gia hạn` → mới: C1, C2, C3

**Agent:** Theo Nghị định 99/2011/NĐ-CP (Điều 22 khoản 2), trong thời hạn 15 ngày làm việc kể từ ngày tiếp nhận yêu cầu bảo vệ quyền lợi người tiêu dùng hợp lệ, cơ quan có thẩm quyền phải trả lời theo quy định tại Điều 26 Luật Bảo vệ quyền lợi người tiêu dùng [struct1000:nd99_2011:p10:o19823:86f6e9534d]. Có gia hạn, nhưng chỉ khi vụ việc phức tạp, và thời hạn gia hạn không quá 15 ngày làm việc [struct1000:nd99_2011:p10:o19823:86f6e9534d]. Lưu ý: Nghị định 99/2011 đã hết hiệu lực từ 01/7/2024 theo phạm vi kho tài liệu; quy định hiện hành cần tra cứu ở văn bản khác.

> `struct1000:nd99_2011:p10:o19823:86f6e9534d` (trang 10): [Nghị định 99/2011/NĐ-CP · Chương IV · Điều 22]
Điều 22. Giải quyết yêu cầu bảo vệ quyền lợi người tiêu dùng
1. Sau khi tiếp nhận yêu cầu bảo vệ quyền lợi người tiêu dùng, cơ quan có
thẩm quyền tiến hành giải quyết yêu cầu. Trường hợp cần thiết, cơ quan có thẩm
quyền có quyền yêu cầu các bên giải trình, cung cấp thêm thông tin, tài liệu phục
vụ cho việc giải quyết yêu cầu bảo vệ quyền lợi người tiêu dùng.
2. Trong thời hạn mười lăm (15) ngày làm việc kể từ ngày tiếp nhận yêu cầu
bảo vệ quyền lợi người tiêu dùng hợp lệ, cơ quan có thẩm quyền phải trả lời theo
quy định tại Điều 26 Luật Bảo vệ qu

_auto: context có evidence = True, citation chứa evidence = True_

---

## t06 · dieu_kien · có đáp án · status `answered`
**Hỏi:** Sản phẩm đã bảo hành bao nhiêu lần trong thời hạn bảo hành mà vẫn không khắc phục được lỗi thì doanh nghiệp phải đổi mới hoặc trả lại tiền?

**Đáp án chuẩn:** Từ 03 (ba) lần trở lên.
**Gold:** [{'source_id': 'luat19_2023', 'page': 23, 'evidence': 'từ 03 lần trở lên trong thời hạn bảo hành mà vẫn không khắc phục được lỗi'}, {'source_id': 'luat59_2010', 'page': 10, 'evidence': 'từ ba lần trở lên trong thời hạn bảo hành mà vẫn không khắc phục được lỗi'}]

- search `sản phẩm bảo hành nhiều lần trong thời hạn bảo hành không khắc phục được lỗi đổi mới hoặc trả lại tiền` → mới: C1, C2, C3

**Agent:** Theo Luật 19/2023/QH15 (hiện hành), doanh nghiệp phải đổi sản phẩm mới tương tự hoặc thu hồi và trả lại tiền khi đã thực hiện bảo hành từ 03 lần trở lên trong thời hạn bảo hành mà vẫn không khắc phục được lỗi [struct1000:luat19_2023:p23:o44830:caf2bc912f]. Luật 59/2010/QH12 (đã thay thế) quy định tương tự với mốc "ba lần trở lên" [struct1000:luat59_2010:p10:o19730:b0d3056cc8].</answer>
<parameter name="citations">["C1", "C2"]

> `struct1000:luat19_2023:p23:o44830:caf2bc912f` (trang 23): [Luật 19/2023/QH15 · Chương II · Điều 30]
đ) Đổi sản phẩm, hàng hóa, linh kiện, phụ kiện mới tương tự hoặc thu hồi sản
phẩm, hàng hóa, linh kiện, phụ kiện và trả lại tiền cho người tiêu dùng trong
trường hợp hết thời gian thực hiện bảo hành mà không sửa chữa được hoặc không
khắc phục được lỗi hoặc trong trường hợp đã thực hiện bảo hành sản phẩm, hàng
hóa, linh kiện, phụ kiện từ 03 lần trở lên trong thời hạn bảo hành mà vẫn không
khắc phục được lỗi;
e) Chịu chi phí sửa chữa, vận chuyển sản phẩm, hàng hóa, linh kiện, phụ kiện
từ nơi ở của người tiêu dùng hoặc nơi sử dụng sản phẩm, hàng hóa, linh

> `struct1000:luat59_2010:p10:o19730:b0d3056cc8` (trang 10): [Luật 59/2010/QH12 · Chương II · Điều 21]
3. Cung cấp cho người tiêu dùng hàng hóa, linh kiện, phụ kiện tương tự để sử
dụng tạm thời hoặc có hình thức giải quyết khác được người tiêu dùng chấp nhận
trong thời gian thực hiện bảo hành;
4. Đổi hàng hóa, linh kiện, phụ kiện mới tương tự hoặc thu hồi hàng hóa, linh
kiện, phụ kiện và trả lại tiền cho người tiêu dùng trong trường hợp hết thời gian thực
hiện bảo hành mà không sửa chữa được hoặc không khắc phục được lỗi.
5. Đổi hàng hóa, linh kiện, phụ kiện mới tương tự hoặc thu hồi hàng hóa và trả
lại tiền cho người tiêu dùng trong trường hợp đã thực 

_auto: context có evidence = True, citation chứa evidence = True_

---

## u04 · thieu_bang_chung · THIẾU BẰNG CHỨNG · status `abstain`
**Hỏi:** Thời hạn bảo hành tối thiểu bắt buộc đối với điện thoại di động là bao nhiêu tháng?

**Lý do thiếu:** Corpus quy định nghĩa vụ bảo hành và cách tính lại thời hạn bảo hành khi đổi/thay linh kiện, nhưng không đặt thời hạn tối thiểu cho bất kỳ loại hàng hóa nào.

- search `thời hạn bảo hành tối thiểu điện thoại di động` → mới: C1, C2, C3
- search `bảo hành hàng hóa thời gian bảo hành tối thiểu theo quy định Nghị định 55/2024` → mới: C4, C5
- search `bảo hành bắt buộc điện thoại di động tối thiểu 12 tháng máy tính xách tay` → mới: C6

**Agent:** Tài liệu hiện có không đủ bằng chứng để xác định thời hạn bảo hành tối thiểu bắt buộc đối với điện thoại di động. Các đoạn tìm được (Luật 19/2023/QH15 Điều 30; Luật 59/2010/QH12 Điều 21; Nghị định 55/2024/NĐ-CP phần mở đầu) chỉ quy định chung về bảo hành theo thỏa thuận hoặc bắt buộc theo pháp luật, cách tính lại thời hạn khi thay thế linh kiện, đổi sản phẩm và trách nhiệm của doanh nghiệp, nhưng không nêu số tháng cụ thể cho điện thoại di động.


---

## u05 · thieu_bang_chung · THIẾU BẰNG CHỨNG · status `abstain`
**Hỏi:** Sàn thương mại điện tử phải khấu trừ thuế thu nhập cá nhân của người bán hàng theo thuế suất bao nhiêu?

**Lý do thiếu:** Corpus chỉ nhắc 'mã số thuế cá nhân' và 'thuế giá trị gia tăng' trong nghĩa vụ cung cấp thông tin (Luật 19/2023 Điều 37); không có quy định khấu trừ thuế hay thuế suất.

- search `sàn thương mại điện tử khấu trừ thuế thu nhập cá nhân của người bán hàng thuế suất` → mới: C1, C2, C3
- search `thuế thu nhập cá nhân người bán hàng trên sàn thương mại điện tử tỷ lệ khấu trừ 0,5% doanh thu` → mới: C4, C5
- search `nền tảng số khấu trừ thuế thu nhập cá nhân thay mặt người bán hàng hóa dịch vụ thương mại điện tử` → mới: C6, C7, C8

**Agent:** Tài liệu hiện có không đủ bằng chứng để trả lời: các đoạn tìm được (Luật 19/2023/QH15 Điều 37, 39; Nghị định 55/2024/NĐ-CP Điều 2) không quy định về việc sàn thương mại điện tử khấu trừ thuế thu nhập cá nhân của người bán hàng, cũng như không nêu thuế suất khấu trừ. Đề nghị tra cứu thêm văn bản về thuế thu nhập cá nhân và hoạt động thương mại điện tử.


---

## u06 · thieu_bang_chung · THIẾU BẰNG CHỨNG · status `abstain`
**Hỏi:** Chương trình khuyến mại giảm giá cho người tiêu dùng được giảm tối đa bao nhiêu phần trăm giá hàng hóa?

**Lý do thiếu:** Không có quy định về khuyến mại hay mức giảm giá tối đa (thuộc Luật Thương mại và nghị định về khuyến mại).

- search `chương trình khuyến mại giảm giá tối đa bao nhiêu phần trăm giá hàng hóa` → mới: C1, C2, C3
- search `khuyến mại hình thức giảm giá không vượt quá 50% giá bán hàng hóa` → mới: C4, C5
- search `khuyến mại giảm giá hàng hóa cùng loại mức giảm tối đa không quá phần trăm` → mới: —

**Agent:** Tài liệu được cung cấp (Luật 59/2010/QH12, Nghị định 99/2011/NĐ-CP, Luật 19/2023/QH15, Nghị định 55/2024/NĐ-CP) không chứa quy định về mức giảm giá tối đa (bao nhiêu phần trăm giá hàng hóa) đối với chương trình khuyến mại giảm giá. Các đoạn tìm được chỉ đề cập đến điều khoản hợp đồng không có hiệu lực, nghĩa vụ của chợ/trung tâm thương mại và trách nhiệm với hàng hóa có khuyết tật, nên tài liệu không đủ bằng chứng để trả lời câu hỏi này.


---

# Context cuối gửi model (để chấm context_grade)

Thang chấm (BENCHMARK.md): **0** = không có evidence; **1** = có nhưng thiếu điều kiện hoặc nguồn; **2** = đủ evidence và nguồn.

## t01 — context (3 đoạn, 2044 ký tự)
**Hỏi:** Theo quy định hiện hành, hòa giải viên thuộc tổ chức hòa giải tranh chấp tiêu dùng cần có kỹ năng và hiểu biết gì?
**Đáp án chuẩn:** Có kỹ năng hòa giải, hiểu biết pháp luật về bảo vệ quyền lợi người tiêu dùng và pháp luật khác có liên quan.

- **C1** `struct1000:luat19_2023:p46:o88049:b8fc1828dd` (Luật 19/2023/QH15, Điều 64, trang 46)
  > [Luật 19/2023/QH15 · Chương V · Điều 64] 3. Trường hợp tranh chấp giữa người tiêu dùng và tổ chức, cá nhân kinh doanh mà có người dân tộc thiểu số thì phải có ít nhất 01 hòa giải viên là người dân tộc thiểu số hoặc là người sử dụng thông thạo tiếng của dân tộc thiểu số đó. Trường hợp không có hòa giải viên đáp ứng yêu cầu tại khoản này thì các bên tham gia hòa giải tự bố trí phiên dịch hoặc đề nghị hòa giải viên bố trí phiên dịch, trừ trường hợp các bên có thỏa thuận khác.
- **C2** `struct1000:luat19_2023:p46:o87407:a734a81d41` (Luật 19/2023/QH15, Điều 64, trang 46)  ← chứa evidence gold
  > [Luật 19/2023/QH15 · Chương V · Điều 64] Điều 64. Hòa giải viên Hòa giải viên hòa giải tranh chấp giữa người tiêu dùng và tổ chức, cá nhân kinh doanh bao gồm: 1. Hòa giải viên theo quy định của pháp luật về hòa giải có liên quan; 2. Hòa giải viên thuộc tổ chức quy định tại điểm a và điểm c khoản 1 Điều 63 của Luật này là công dân Việt Nam đáp ứng đủ các điều kiện sau đây: a) Có năng lực hành vi dân sự đầy đủ; b) Có phẩm chất đạo đức tốt, trung thực, có uy tín; c) Có kỹ năng hòa giải, hiểu biết pháp luật về bảo vệ quyền lợi người tiêu dùng và pháp luật khác có liên quan; d) Không đang trong thời gian bị truy cứu trách nhiệm hình sự hoặc đã bị kết án mà chưa được xóa án tích.
- **C3** `struct1000:luat19_2023:p45:o86700:780a5f6dc9` (Luật 19/2023/QH15, Điều 63, trang 45)
  > [Luật 19/2023/QH15 · Chương V · Điều 63] Điều 63. Tổ chức hòa giải 1. Tổ chức hòa giải tranh chấp giữa người tiêu dùng và tổ chức, cá nhân kinh doanh bao gồm: a) Tổ chức xã hội tham gia bảo vệ quyền lợi người tiêu dùng; b) Tổ chức hòa giải theo quy định của pháp luật về hòa giải thương mại, pháp luật về hòa giải tại cơ sở, pháp luật về hòa giải tại tòa án; c) Tổ chức khác có chức năng hòa giải tranh chấp giữa người tiêu dùng và tổ chức, cá nhân kinh doanh theo quy định của pháp luật. 2. Tổ chức hòa giải theo quy định tại điểm a và điểm c khoản 1 Điều này có trách nhiệm công nhận, công bố Danh sách hòa giải viên đủ điều kiện theo quy định của Luật này và chỉ định các hòa giải viên tham gia thực hiện việc hòa giải theo yêu cầu của các bên.

---

## t02 — context (3 đoạn, 2566 ký tự)
**Hỏi:** Với hàng hóa bán năm 2015 (áp dụng luật cũ), khi phát hiện khuyết tật, nhà sản xuất phải thông báo công khai việc thu hồi trên báo hoặc đài như thế nào?
**Đáp án chuẩn:** Ít nhất 05 số liên tiếp trên báo ngày hoặc 05 ngày liên tiếp trên đài phát thanh, truyền hình tại địa phương nơi hàng hóa lưu thông.

- **C1** `struct1000:luat59_2010:p11:o20713:5dcc945667` (Luật 59/2010/QH12, Điều 22, trang 11)  ← chứa evidence gold
  > [Luật 59/2010/QH12 · Chương II · Điều 22] Điều 22. Trách nhiệm thu hồi hàng hóa có khuyết tật Khi phát hiện hàng hóa có khuyết tật, tổ chức, cá nhân sản xuất, nhập khẩu hàng hóa có trách nhiệm: 1. Kịp thời tiến hành mọi biện pháp cần thiết để ngừng việc cung cấp hàng hóa có khuyết tật trên thị trường; 2. Thông báo công khai về hàng hóa có khuyết tật và việc thu hồi hàng hóa đó ít nhất 05 số liên tiếp trên báo ngày hoặc 05 ngày liên tiếp trên đài phát thanh, truyền hình tại địa phương mà hàng hóa đó được lưu thông với các nội dung sau đây: a) Mô tả hàng hóa phải thu hồi; b) Lý do thu hồi hàng hóa và cảnh báo nguy cơ thiệt hại do khuyết tật của hàng hóa gây ra; c) Thời gian, địa điểm, phương thức thu hồi hàng hóa; d) Thời gian, phương thức khắc phục khuyết tật của hàng hóa; đ) Các biện pháp cần thiết để bảo vệ quyền lợi người tiêu dùng trong quá trình thu hồi hàng hóa;
- **C2** `struct1000:luat59_2010:p11:o21551:4652bf1c96` (Luật 59/2010/QH12, Điều 22, trang 11)
  > [Luật 59/2010/QH12 · Chương II · Điều 22] 3. Thực hiện việc thu hồi hàng hóa có khuyết tật đúng nội dung đã thông báo công khai và chịu các chi phí phát sinh trong quá trình thu hồi; 4. Báo cáo kết quả cho cơ quan quản lý nhà nước về bảo vệ quyền lợi người tiêu dùng cấp tỉnh nơi thực hiện thu hồi hàng hóa có khuyết tật sau khi hoàn thành việc thu hồi; trường hợp việc thu hồi hàng hóa có khuyết tật được tiến hành trên địa bàn từ hai tỉnh trở lên thì báo cáo kết quả cho cơ quan quản lý nhà nước về bảo vệ quyền lợi người tiêu dùng ở trung ương.
- **C3** `struct1000:luat59_2010:p11:o22057:afb8efe8be` (Luật 59/2010/QH12, Điều 23, trang 11,12)
  > [Luật 59/2010/QH12 · Chương II · Điều 23] Điều 23. Trách nhiệm bồi thường thiệt hại do hàng hóa có khuyết tật gây ra 1. Tổ chức, cá nhân kinh doanh hàng hóa có trách nhiệm bồi thường thiệt hại trong trường hợp hàng hóa có khuyết tật do mình cung cấp gây thiệt hại đến tính mạng, sức khỏe, tài sản của người tiêu dùng, kể cả khi tổ chức, cá nhân đó không biết hoặc không có lỗi trong việc phát sinh khuyết tật, trừ trường hợp quy định tại Điều 24 của Luật này. 2. Tổ chức, cá nhân kinh doanh hàng hóa quy định tại khoản 1 Điều này bao gồm: a) Tổ chức, cá nhân sản xuất hàng hóa; b) Tổ chức, cá nhân nhập khẩu hàng hóa; c) Tổ chức, cá nhân gắn tên thương mại lên hàng hóa hoặc sử dụng nhãn hiệu, chỉ dẫn thương mại cho phép nhận biết đó là tổ chức, cá nhân sản xuất, nhập khẩu hàng hóa; d) Tổ chức, cá nhân trực tiếp cung cấp hàng hóa có khuyết tật cho người tiêu dùng trong trường hợp không xác định được tổ chức, cá nhân có trách nhiệm bồi thường thiệt hại quy định tại các điểm a, b và c khoản này.

---

## t03 — context (4 đoạn, 3042 ký tự)
**Hỏi:** Tổ chức xã hội khởi kiện vụ án dân sự vì lợi ích công cộng để bảo vệ người tiêu dùng có phải chịu án phí không?
**Đáp án chuẩn:** Không phải nộp tiền tạm ứng án phí và không phải chịu án phí.

- **C1** `struct1000:luat19_2023:p40:o77136:14e8c73743` (Luật 19/2023/QH15, Điều 50, trang 40)
  > [Luật 19/2023/QH15 · Chương IV · Điều 50] 2. Tổ chức xã hội tham gia bảo vệ quyền lợi người tiêu dùng có quyền tự mình khởi kiện vụ án dân sự về bảo vệ quyền lợi người tiêu dùng vì lợi ích công cộng khi có đủ các điều kiện sau đây: a) Được thành lập hợp pháp theo quy định của pháp luật; b) Có tôn chỉ, mục đích hoạt động vì quyền lợi người tiêu dùng hoặc vì lợi ích công cộng liên quan đến quyền lợi người tiêu dùng; c) Có thời gian hoạt động tối thiểu 01 năm kể từ ngày tổ chức xã hội được thành lập đến ngày tổ chức xã hội thực hiện quyền tự khởi kiện; d) Có phạm vi hoạt động từ cấp huyện trở lên.
- **C2** `struct1000:nd99_2011:p11:o23052:276160613a` (Nghị định 99/2011/NĐ-CP, Điều 25, trang 11)
  > [Nghị định 99/2011/NĐ-CP · Chương V · Điều 25] Điều 25. Nghĩa vụ của tổ chức xã hội tham gia bảo vệ quyền lợi người tiêu dùng khi tự mình khởi kiện vụ án bảo vệ người tiêu dùng vì lợi ích công cộng Khi tự mình khởi kiện vụ án bảo vệ quyền lợi người tiêu dùng vì lợi ích công cộng, tổ chức xã hội tham gia bảo vệ quyền lợi người tiêu dùng có nghĩa vụ sau: 1. Thông báo thông tin về nội dung vụ án theo quy định tại Điều 44 Luật Bảo vệ quyền lợi người tiêu dùng. 2. Đảm bảo quyền tham gia vụ án của những người tiêu dùng có liên quan đến vụ án. 3. Chịu các chi phí phát sinh trong quá trình khởi kiện.
- **C3** `struct1000:luat19_2023:p48:o91525:df6fcf7de1` (Luật 19/2023/QH15, Điều 71, trang 48)  ← chứa evidence gold
  > [Luật 19/2023/QH15 · Chương V · Điều 71] Điều 71. Án phí đối với vụ án dân sự về bảo vệ quyền lợi người tiêu dùng 1. Án phí đối với vụ án dân sự về bảo vệ quyền lợi người tiêu dùng được thực hiện theo quy định của pháp luật về án phí, lệ phí Tòa án và quy định của Luật này. 2. Người tiêu dùng khởi kiện vụ án dân sự bảo vệ quyền, lợi ích hợp pháp của mình, tổ chức xã hội tham gia bảo vệ quyền lợi người tiêu dùng đại diện cho người tiêu dùng theo ủy quyền khởi kiện vụ án dân sự về bảo vệ quyền lợi người tiêu dùng không phải nộp tiền tạm ứng án phí. 3. Tổ chức xã hội tham gia bảo vệ quyền lợi người tiêu dùng khởi kiện vụ án dân sự về bảo vệ quyền lợi người tiêu dùng vì lợi ích công cộng không phải nộp tiền tạm ứng án phí, không phải chịu án phí.
- **C4** `struct1000:nd99_2011:p11:o22204:3aca539189` (Nghị định 99/2011/NĐ-CP, Điều 24, trang 11)
  > [Nghị định 99/2011/NĐ-CP · Chương V · Điều 24] Chương V TỔ CHỨC XÃ HỘI THAM GIA HOẠT ĐỘNG BẢO VỆ QUYỀN LỢI NGƯỜI TIÊU DÙNG Mục 1 KHỞI KIỆN VỤ ÁN BẢO VỆ QUYỀN LỢI NGƯỜI TIÊU DÙNG Điều 24. Điều kiện của tổ chức xã hội tham gia bảo vệ quyền lợi người tiêu dùng được quyền tự mình khởi kiện vụ án bảo vệ người tiêu dùng vì lợi ích công cộng Tổ chức xã hội tham gia bảo vệ quyền lợi người tiêu dùng được quyền tự mình khởi kiện vụ án bảo vệ quyền lợi người tiêu dùng vì lợi ích công cộng khi có đủ các điều kiện sau đây: 1. Được thành lập hợp pháp theo quy định của pháp luật. 2. Có tôn chỉ, mục đích hoạt động vì quyền lợi người tiêu dùng hoặc vì lợi ích công cộng liên quan đến quyền lợi người tiêu dùng. 3. Có thời gian hoạt động tối thiểu là ba (03) năm tính từ ngày tổ chức xã hội được thành lập đến ngày tổ chức xã hội thực hiện quyền tự khởi kiện. 4. Có phạm vi hoạt động từ cấp tỉnh trở lên.

---

## t04 — context (6 đoạn, 4978 ký tự)
**Hỏi:** Nền tảng số lớn có chức năng tìm kiếm phải công khai điều gì về cách sắp xếp thứ tự hiển thị sản phẩm?
**Đáp án chuẩn:** Công bố công khai tiêu chí xác định ưu tiên hiển thị sản phẩm, hàng hóa, dịch vụ; nội dung có thu phí/được tài trợ phải công khai tại kết quả tìm kiếm.

- **C1** `struct1000:nd55_2024:p15:o28119:fd491db37d` (Nghị định 55/2024/NĐ-CP, Điều 23, trang 15)  ← chứa evidence gold
  > [Nghị định 55/2024/NĐ-CP · Chương VI · Điều 23] Điều 23. Trách nhiệm của tổ chức thiết lập, vận hành nền tảng số lớn 1. Công bố công khai tiêu chí xác định ưu tiên hiển thị sản phẩm, hàng hóa, dịch vụ nếu nền tảng số có chức năng tìm kiếm. Trường hợp nội dung hiển thị là nội dung có thu phí hoặc được tài trợ thì phải công khai tại kết quả tìm kiếm sản phẩm, hàng hóa, dịch vụ. Việc xây dựng và công bố áp dụng các tiêu chí để xác định việc ưu tiên hiển thị sản phẩm, hàng hóa, dịch vụ khi sử dụng chức năng tìm kiếm phải tuân thủ các quy định của pháp luật có liên quan.
- **C2** `struct1000:luat19_2023:p31:o61053:8d0a648bcd` (Luật 19/2023/QH15, Điều 39, trang 31,32)
  > [Luật 19/2023/QH15 · Chương III · Điều 39] e) Chỉ định, công bố công khai đầu mối tiếp nhận và giải quyết phản ánh, yêu cầu, khiếu nại của người tiêu dùng liên quan đến sản phẩm, hàng hóa, dịch vụ, nội dung thông tin trên nền tảng số trung gian; tiếp nhận và giải quyết phản ánh, yêu cầu, khiếu nại của người tiêu dùng đối với tổ chức thiết lập, vận hành nền tảng số trung gian; g) Có biện pháp cho phép hiển thị ưu tiên đánh giá, phản ánh, kiến nghị của tổ chức xã hội tham gia bảo vệ quyền lợi người tiêu dùng hoặc tổ chức đánh giá tín nhiệm theo quy định của pháp luật; h) Trực tiếp lưu trữ thông tin hoặc cung cấp giải pháp lưu trữ thông tin về sản phẩm, hàng hóa, dịch vụ và các giao dịch liên quan, cho phép người tiêu dùng truy cập, truy vết, tải, lưu trữ và in hóa đơn, chứng từ, tài liệu liên quan đến giao dịch trên nền tảng số trung gian mà mình quản lý; i) Minh bạch hoạt động quảng cáo trên không gian mạng theo quy định của pháp luật trong trường hợp có hoạt động quảng cáo;
- **C3** `struct1000:luat19_2023:p11:o20451:99c865484a` (Luật 19/2023/QH15, Điều 10, trang 11)
  > [Luật 19/2023/QH15 · Chương I · Điều 10] 3. Tổ chức, cá nhân kinh doanh thiết lập, vận hành, cung cấp dịch vụ nền tảng số bị nghiêm cấm thực hiện các hành vi sau đây: a) Ép buộc hoặc ngăn cản người tiêu dùng đăng ký sử dụng hoặc sử dụng nền tảng số trung gian khác như là điều kiện bắt buộc để sử dụng dịch vụ; b) Hạn chế quyền lựa chọn của người tiêu dùng thông qua việc sắp xếp ưu tiên lựa chọn sản phẩm, hàng hóa, dịch vụ giữa các tổ chức, cá nhân kinh doanh cung cấp trên nền tảng số mà không công khai tiêu chí lựa chọn; c) Sử dụng biện pháp ngăn hiển thị hoặc hiển thị không trung thực kết quả phản hồi, đánh giá của người tiêu dùng về sản phẩm, hàng hóa, dịch vụ, tổ chức, cá nhân kinh doanh trên nền tảng số, trừ trường hợp phản hồi, đánh giá đó vi phạm quy định của pháp luật, trái đạo đức xã hội; d) Sử dụng biện pháp ngăn cản đăng ký, hoạt động, đánh giá, hiển thị phản hồi của tổ chức xã hội tham gia bảo vệ quyền lợi người tiêu dùng;
- **C4** `struct1000:luat19_2023:p50:o95596:a1dbcf2434` (Luật 19/2023/QH15, Điều 75, trang 50)
  > [Luật 19/2023/QH15 · Chương VI · Điều 75] 3. Tổ chức hoạt động khảo sát, thử nghiệm; công bố kết quả khảo sát, thử nghiệm chất lượng sản phẩm, hàng hóa, dịch vụ; thông tin, cảnh báo cho người tiêu dùng về sản phẩm, hàng hóa, dịch vụ trong lĩnh vực được phân công quản lý. 4. Xây dựng cơ sở dữ liệu thông tin quốc gia về bảo vệ quyền lợi người tiêu dùng. 5. Thực hiện việc giao nhiệm vụ cho tổ chức xã hội có tôn chỉ, mục đích tham gia bảo vệ quyền lợi người tiêu dùng theo quy định tại khoản 2 Điều 53 của Luật này và quy định của luật khác có liên quan. 6. Quản lý hoạt động bảo vệ quyền lợi người tiêu dùng của tổ chức xã hội tham gia bảo vệ quyền lợi người tiêu dùng, tổ chức hòa giải về bảo vệ quyền lợi người tiêu dùng theo quy định của pháp luật. 7. Xây dựng cơ chế phối hợp với các Bộ, cơ quan ngang Bộ có liên quan để triển khai các hoạt động về bảo vệ quyền lợi người tiêu dùng theo thẩm quyền.
- **C5** `struct1000:luat19_2023:p1:o247:934eba60aa` (Luật 19/2023/QH15, Điều 1, trang 1)
  > [Luật 19/2023/QH15 · Chương I · Điều 1] Chương I NHỮNG QUY ĐỊNH CHUNG Điều 1. Phạm vi điều chỉnh Luật này quy định về nguyên tắc, chính sách bảo vệ quyền lợi người tiêu dùng; quyền và nghĩa vụ của người tiêu dùng; trách nhiệm của tổ chức, cá nhân kinh doanh đối với người tiêu dùng; hoạt động bảo vệ quyền lợi người tiêu dùng của cơ quan, tổ chức; giải quyết tranh chấp giữa người tiêu dùng và tổ chức, cá nhân kinh doanh; quản lý nhà nước về bảo vệ quyền lợi người tiêu dùng.
- **C6** `struct1000:luat19_2023:p5:o7690:35c36474e9` (Luật 19/2023/QH15, Điều 6, trang 5)
  > [Luật 19/2023/QH15 · Chương I · Điều 6] Điều 6. Nguyên tắc bảo vệ quyền lợi người tiêu dùng 1. Bảo vệ quyền lợi người tiêu dùng là trách nhiệm của Nhà nước, tổ chức, cá nhân và toàn xã hội. 2. Quyền, lợi ích hợp pháp của người tiêu dùng được công nhận, tôn trọng, bảo đảm và bảo vệ theo quy định của pháp luật. 3. Bảo vệ quyền lợi người tiêu dùng phải được chủ động thực hiện kịp thời, công bằng, minh bạch, đúng pháp luật. 4. Hoạt động bảo vệ quyền lợi người tiêu dùng không được xâm phạm đến lợi ích của Nhà nước, quyền, lợi ích hợp pháp của tổ chức, cá nhân kinh doanh và tổ chức, cá nhân khác. 5. Bảo đảm công bằng, bình đẳng, không phân biệt về giới, tự nguyện, không vi phạm pháp luật, không trái với thuần phong mỹ tục và đạo đức xã hội trong giao dịch giữa người tiêu dùng và tổ chức, cá nhân kinh doanh.

---

## t05 — context (3 đoạn, 2167 ký tự)
**Hỏi:** Theo Nghị định 99/2011, cơ quan có thẩm quyền phải trả lời yêu cầu bảo vệ quyền lợi người tiêu dùng hợp lệ trong bao lâu, và có được gia hạn không?
**Đáp án chuẩn:** 15 ngày làm việc kể từ ngày tiếp nhận yêu cầu hợp lệ; vụ việc phức tạp có thể gia hạn nhưng không quá 15 ngày làm việc.

- **C1** `struct1000:nd99_2011:p10:o19823:86f6e9534d` (Nghị định 99/2011/NĐ-CP, Điều 22, trang 10)  ← chứa evidence gold
  > [Nghị định 99/2011/NĐ-CP · Chương IV · Điều 22] Điều 22. Giải quyết yêu cầu bảo vệ quyền lợi người tiêu dùng 1. Sau khi tiếp nhận yêu cầu bảo vệ quyền lợi người tiêu dùng, cơ quan có thẩm quyền tiến hành giải quyết yêu cầu. Trường hợp cần thiết, cơ quan có thẩm quyền có quyền yêu cầu các bên giải trình, cung cấp thêm thông tin, tài liệu phục vụ cho việc giải quyết yêu cầu bảo vệ quyền lợi người tiêu dùng. 2. Trong thời hạn mười lăm (15) ngày làm việc kể từ ngày tiếp nhận yêu cầu bảo vệ quyền lợi người tiêu dùng hợp lệ, cơ quan có thẩm quyền phải trả lời theo quy định tại Điều 26 Luật Bảo vệ quyền lợi người tiêu dùng. Trường hợp vụ việc phức tạp, thời hạn trả lời có thể được gia hạn nhưng không quá mười lăm (15) ngày làm việc.
- **C2** `struct1000:nd99_2011:p1:o0:b5902ad75e` (Nghị định 99/2011/NĐ-CP, Điều 0, trang 1)
  > [Nghị định 99/2011/NĐ-CP · Phần mở đầu] CHÍNH PHỦ CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM Độc lập à Tự do à Hạnh phúc Số: 99/2011/NĐqCP Hà Nội, ngày 27 tháng 10 năm 2011 NGHỊ ĐỊNH Quy định chi tiết và hướng dẫn thi hành một số điều của Luật Bảo vệ quyền lợi người tiêu dùng CHÍNH PHỦ Căn cứ Luật Tổ chức Chính phủ ngày 25 tháng 12 năm 2001; Căn cứ Luật số 59/2010/QH12 về Bảo vệ quyền lợi người tiêu dùng ngày 17 tháng 11 năm 2010; Xét đề nghị của Bộ trưởng Bộ Công thương, NGHỊ ĐỊNH:
- **C3** `struct1000:nd99_2011:p9:o18244:7a5cc2ba37` (Nghị định 99/2011/NĐ-CP, Điều 20, trang 9)
  > [Nghị định 99/2011/NĐ-CP · Chương IV · Điều 20] Chương IV GIẢI QUYẾT YÊU CẦU BẢO VỆ QUYỀN LỢI NGƯỜI TIÊU DÙNG Điều 20. Hình thức, nội dung của yêu cầu bảo vệ quyền lợi người tiêu dùng 1. Người tiêu dùng, tổ chức xã hội tham gia bảo vệ quyền lợi người tiêu dùng có quyền yêu cầu cơ quan quản lý nhà nước về bảo vệ quyền lợi người tiêu dùng theo quy định tại Điều 25 Luật Bảo vệ quyền lợi người tiêu dùng. Việc yêu cầu có thể được thực hiện bằng văn bản hoặc yêu cầu trực tiếp. 2. Yêu cầu bảo vệ quyền lợi người tiêu dùng phải có các nội dung sau: a) Thông tin về tổ chức, cá nhân kinh doanh vi phạm; b) Thông tin về tổ chức xã hội hoặc người tiêu dùng yêu cầu; c) Nội dung vụ việc; d) Yêu cầu cụ thể của người tiêu dùng, tổ chức xã hội tham gia bảo vệ quyền lợi người tiêu dùng; đ) Tài liệu, chứng cứ kèm theo.

---

## t06 — context (3 đoạn, 2795 ký tự)
**Hỏi:** Sản phẩm đã bảo hành bao nhiêu lần trong thời hạn bảo hành mà vẫn không khắc phục được lỗi thì doanh nghiệp phải đổi mới hoặc trả lại tiền?
**Đáp án chuẩn:** Từ 03 (ba) lần trở lên.

- **C1** `struct1000:luat19_2023:p23:o44830:caf2bc912f` (Luật 19/2023/QH15, Điều 30, trang 23)  ← chứa evidence gold
  > [Luật 19/2023/QH15 · Chương II · Điều 30] đ) Đổi sản phẩm, hàng hóa, linh kiện, phụ kiện mới tương tự hoặc thu hồi sản phẩm, hàng hóa, linh kiện, phụ kiện và trả lại tiền cho người tiêu dùng trong trường hợp hết thời gian thực hiện bảo hành mà không sửa chữa được hoặc không khắc phục được lỗi hoặc trong trường hợp đã thực hiện bảo hành sản phẩm, hàng hóa, linh kiện, phụ kiện từ 03 lần trở lên trong thời hạn bảo hành mà vẫn không khắc phục được lỗi; e) Chịu chi phí sửa chữa, vận chuyển sản phẩm, hàng hóa, linh kiện, phụ kiện từ nơi ở của người tiêu dùng hoặc nơi sử dụng sản phẩm, hàng hóa, linh kiện, phụ kiện đến nơi bảo hành và từ nơi bảo hành đến nơi ở của người tiêu dùng hoặc nơi sử dụng sản phẩm, hàng hóa, linh kiện, phụ kiện; g) Chịu trách nhiệm về việc bảo hành sản phẩm, hàng hóa, linh kiện, phụ kiện cho người tiêu dùng cả trong trường hợp ủy quyền hoặc thuê tổ chức, cá nhân khác thực hiện việc bảo hành.
- **C2** `struct1000:luat59_2010:p10:o19730:b0d3056cc8` (Luật 59/2010/QH12, Điều 21, trang 10)  ← chứa evidence gold
  > [Luật 59/2010/QH12 · Chương II · Điều 21] 3. Cung cấp cho người tiêu dùng hàng hóa, linh kiện, phụ kiện tương tự để sử dụng tạm thời hoặc có hình thức giải quyết khác được người tiêu dùng chấp nhận trong thời gian thực hiện bảo hành; 4. Đổi hàng hóa, linh kiện, phụ kiện mới tương tự hoặc thu hồi hàng hóa, linh kiện, phụ kiện và trả lại tiền cho người tiêu dùng trong trường hợp hết thời gian thực hiện bảo hành mà không sửa chữa được hoặc không khắc phục được lỗi. 5. Đổi hàng hóa, linh kiện, phụ kiện mới tương tự hoặc thu hồi hàng hóa và trả lại tiền cho người tiêu dùng trong trường hợp đã thực hiện bảo hành hàng hóa, linh kiện, phụ kiện từ ba lần trở lên trong thời hạn bảo hành mà vẫn không khắc phục được lỗi; 6. Chịu chi phí sửa chữa, vận chuyển hàng hóa, linh kiện, phụ kiện đến nơi bảo hành và từ nơi bảo hành đến nơi cư trú của người tiêu dùng;
- **C3** `struct1000:luat19_2023:p23:o43993:718ebcc363` (Luật 19/2023/QH15, Điều 30, trang 23)
  > [Luật 19/2023/QH15 · Chương II · Điều 30] c) Cung cấp cho người tiêu dùng văn bản tiếp nhận bảo hành hoặc hình thức tiếp nhận bảo hành tương đương khác, trong đó ghi rõ thời gian thực hiện bảo hành. Thời gian thực hiện bảo hành không tính vào thời hạn bảo hành sản phẩm, hàng hóa, linh kiện, phụ kiện. Trường hợp tổ chức, cá nhân kinh doanh thay thế linh kiện, phụ kiện thì thời hạn bảo hành linh kiện, phụ kiện đó được tính lại từ thời điểm thay thế linh kiện, phụ kiện. Trường hợp tổ chức, cá nhân kinh doanh đổi sản phẩm, hàng hóa mới thì thời hạn bảo hành sản phẩm, hàng hóa đó được tính lại từ thời điểm đổi mới sản phẩm, hàng hóa; d) Cung cấp cho người tiêu dùng sản phẩm, hàng hóa, linh kiện, phụ kiện tương tự để sử dụng tạm thời hoặc có hình thức giải quyết phù hợp theo thỏa thuận giữa người tiêu dùng và tổ chức, cá nhân kinh doanh trong thời gian thực hiện bảo hành;

---
