
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_CODE = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Shopee Indonesia | Agen Smith</title>
    <style>
        :root { --shopee-orange: #ee4d2d; }
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: sans-serif; }
        body { background: #f5f5f5; padding-bottom: 80px; color: #333; }
        .header { background: white; padding: 12px; display: flex; align-items: center; position: sticky; top: 0; z-index: 100; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
        .section { background: white; padding: 15px; margin-bottom: 8px; }
        
        /* Slider Manual (Slide Pakai Jari) */
        .slider-container { width: 100%; overflow-x: auto; scroll-snap-type: x mandatory; display: flex; background: white; -webkit-overflow-scrolling: touch; }
        .slider-container::-webkit-scrollbar { display: none; }
        .slider-wrapper { display: flex; }
        .slider-wrapper img { width: 100vw; scroll-snap-align: start; flex-shrink: 0; object-fit: cover; display: block; }

        .price { color: var(--shopee-orange); font-size: 24px; font-weight: bold; }
        
        /* Shop Profile (Sesuai Gambar Yang Lu Kasih) */
        .shop-profile { display: flex; align-items: center; gap: 12px; }
        .shop-img { width: 50px; height: 50px; border-radius: 50%; border: 1px solid #eee; }
        .shop-stats { display: flex; gap: 10px; margin-top: 15px; border-top: 1px solid #f0f0f0; padding-top: 12px; text-align: center; }
        .stat-val { color: var(--shopee-orange); font-weight: bold; font-size: 14px; }
        .stat-lab { font-size: 10px; color: #888; }

        .desc-title { font-weight: bold; font-size: 14px; margin-bottom: 10px; border-left: 3px solid var(--shopee-orange); padding-left: 8px; }
        .desc-box { font-size: 13px; color: #555; line-height: 1.6; }

        .v-item { display: inline-block; border: 1px solid #ddd; padding: 8px 12px; margin: 4px; font-size: 12px; border-radius: 2px; cursor: pointer; }
        .v-item.active { border-color: var(--shopee-orange); color: var(--shopee-orange); background: #fff5f2; }
        
        .qty-container { display: flex; align-items: center; gap: 15px; margin-top: 20px; border-top: 1px solid #f0f0f0; padding-top: 15px; }
        .qty-btn { width: 32px; height: 32px; border: 1px solid #ddd; background: white; font-size: 20px; display: flex; align-items: center; justify-content: center; }

        .review-item { border-bottom: 1px solid #eee; padding: 15px 0; }
        .review-user { font-weight: bold; font-size: 12px; display: flex; justify-content: space-between; }
        .stars { color: #ffce3d; font-size: 10px; }
        .review-text { font-size: 13px; color: #333; margin: 6px 0; }
        .review-img { width: 80px; height: 80px; object-fit: cover; border-radius: 4px; margin-right: 5px; border: 1px solid #eee; }
        .review-time { font-size: 10px; color: #999; }

        .modal-full { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: white; display: none; flex-direction: column; z-index: 1000; }
        .modal-header { padding: 15px; display: flex; align-items: center; border-bottom: 1px solid #eee; font-size: 17px; }
        .form-group { border-bottom: 1px solid #f0f0f0; padding: 15px; }
        .form-group input, .form-group textarea { width: 100%; border: none; outline: none; font-size: 15px; }
        
        .modal-pay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); display: none; justify-content: center; align-items: center; z-index: 1100; }
        .pay-card { background: white; width: 90%; border-radius: 8px; padding: 20px; text-align: center; }

        .btn-main { background: #ff4721; color: white; border: none; width: 90%; padding: 12px; margin: 10px auto; display: block; border-radius: 4px; font-weight: bold; text-transform: uppercase; }
        .fixed-footer { position: fixed; bottom: 0; width: 100%; background: white; padding: 10px; border-top: 1px solid #eee; }
    </style>
</head>
<body>
    <div class="header"><b>← Smith Cigarettes Official</b></div>
    
    <div class="slider-container">
        <div class="slider-wrapper">
            <img src="https://i.ibb.co.com/6xjzRm1/Screenshot-20250213-231139.png">
            <img src="https://i.ibb.co.com/b5dbYQ4Y/image.jpg">
            <img src="https://i.ibb.co.com/7tqDWD1h/image.jpg">
            <img src="https://i.ibb.co.com/3yqzfXSs/image.jpg">
            <img src="https://i.ibb.co.com/HLh0c65s/image.jpg">
            <img src="https://i.ibb.co.com/0R969RJq/image.jpg">
            <img src="https://i.ibb.co.com/cS7xZ1jQ/image.jpg">
        </div>
    </div>

    <div class="section">
        <div class="price">Rp106.000</div>
        <div style="font-size:16px; margin:8px 0; font-weight:500;">Rokok SMITH Premium Flavor - Bakau Pilihan High Quality</div>
    </div>

    <div class="section">
        <div class="shop-profile">
            <img src="https://i.ibb.co.com/YBvL003X/image.jpg" class="shop-img"> 
            <div style="flex:1">
                <h4>Agen Smith</h4> 
                <p style="font-size:11px; color:green;">● Online</p>
            </div>
            <div style="border:1px solid var(--shopee-orange); color:var(--shopee-orange); padding:4px 8px; font-size:12px; border-radius:2px;">Kunjungi Toko</div>
        </div>
        <div class="shop-stats">
            <div style="flex:1"><div class="stat-val">1.277</div><div class="stat-lab">Produk Terjual</div></div>
            <div style="flex:1"><div class="stat-val">4.9</div><div class="stat-lab">Penilaian</div></div>
            <div style="flex:1"><div class="stat-val">1.549 rb</div><div class="stat-lab">Pengikut</div></div>
        </div>
    </div>

    <div class="section">
        <div class="desc-title">Deskripsi Produk</div>
        <div class="desc-box">
            <b>Smith Cigarettes</b> hadir dengan kualitas bakau pilihan yang diracik khusus untuk cita rasa elegan. Sangat cocok bagi Anda penikmat tembakau berkualitas tinggi.<br><br>
            <b>Pilihan Varian Rasa:</b><br>
            - 🔴 <b>Smith Merah:</b> Rasa Original Bold yang mantap.<br>
            - 🟢 <b>Smith Hijau:</b> Sensasi Menthol yang dingin dan segar.<br>
            - ⚪ <b>Smith Silver:</b> Rasa Smooth dan ringan.<br>
            - ⚫ <b>Smith Bold:</b> Racikan khusus lebih kuat.<br>
            - 🔘 <b>Smith Abu-abu:</b> Cita rasa klasik premium.<br>
            - 🍋 <b>Smith Lemon:</b> Fresh dengan aroma citrus.<br>
            - 🍉 <b>Smith Melon:</b> Manis buah yang menyegarkan.
        </div>
    </div>

    <div class="section">
        <p style="font-size:13px; font-weight:bold; margin-bottom:10px;">Pilih Varian:</p>
        <div class="v-item" onclick="s(this)">Smith Merah</div><div class="v-item" onclick="s(this)">Smith Hijau</div><div class="v-item" onclick="s(this)">Smith Silver</div><div class="v-item" onclick="s(this)">Smith Bold</div><div class="v-item" onclick="s(this)">Smith Abu-abu</div><div class="v-item" onclick="s(this)">Smith Lemon</div><div class="v-item" onclick="s(this)">Smith Melon</div>
        <div class="qty-container">
            <span style="flex:1; font-size:13px;">Jumlah Produk:</span>
            <button class="qty-btn" onclick="updQty(-1)">-</button><span id="qty-val" style="font-weight:bold; width:30px; text-align:center;">1</span><button class="qty-btn" onclick="updQty(1)">+</button>
        </div>
    </div>

    <div class="section">
        <div style="font-weight:bold; font-size:14px; margin-bottom:10px;">PENILAIAN PRODUK (50)</div>
        <div id="review-list">
            <div class="review-item"><div class="review-user">T***r <span class="stars">⭐⭐⭐⭐⭐</span></div><div class="review-text">Tester beli 1 ternyata sesuai barang original amanah.</div><img src="https://i.ibb.co.com/qF2kB0mw/image.jpg" class="review-img"><div class="review-time">14-02-2026</div></div>
            <div class="review-item"><div class="review-user">A***n <span class="stars">⭐⭐⭐⭐⭐</span></div><div class="review-text">Mantap aman, Datang dengan cepat</div><img src="https://i.ibb.co.com/j9NsCdp8/image.jpg" class="review-img"><div class="review-time">10-02-2026</div></div>
            <div class="review-item"><div class="review-user">B***i <span class="stars">⭐⭐⭐⭐⭐</span></div><div class="review-text">Barang sesuai pesanan dan kualitas mantap.</div><img src="https://i.ibb.co.com/rKHVcbgn/image.jpg" class="review-img"><div class="review-time">05-02-2026</div></div>
            <div class="review-item"><div class="review-user">S***h <span class="stars">⭐⭐⭐⭐⭐</span></div><div class="review-text">Seller sangat amanah pengiriman rapih.</div><img src="https://i.ibb.co.com/n8N71QGw/image.jpg" class="review-img"><div class="review-time">01-02-2026</div></div>
            <div class="review-item"><div class="review-user">P***h <span class="stars">⭐⭐⭐⭐⭐</span></div><div class="review-text">Packing rapih cepat sampai</div><img src="https://i.ibb.co.com/ZzCcPNJv/image.jpg" class="review-img"><div class="review-time">28-01-2026</div></div>
            <div class="review-item"><div class="review-user">S***t <span class="stars">⭐⭐⭐⭐⭐</span></div><div class="review-text">Barang sudah mendarat dengan selamat.. rasa super mantap..</div><img src="https://i.ibb.co.com/9HF9S7Jv/image.jpg" class="review-img"><div class="review-time">22-01-2026</div></div>
            <div class="review-item"><div class="review-user">C***k <span class="stars">⭐⭐⭐⭐⭐</span></div><div class="review-text">Udah coba variannya dan rasanya cocok buat harian.</div><img src="https://i.ibb.co.com/chNx6xbx/image.jpg" class="review-img"><div class="review-time">15-01-2026</div></div>
            <div class="review-item"><div class="review-user">M***b <span class="stars">⭐⭐⭐⭐⭐</span></div><div class="review-text">respon cepat, pengiriman cepat, barang sesuai.</div><img src="https://i.ibb.co.com/SDddgdg5/image.jpg" class="review-img"><div class="review-time">10-01-2026</div></div>
            <div class="review-item"><div class="review-user">B***s <span class="stars">⭐⭐⭐⭐⭐</span></div><div class="review-text">Rasanya mantap bos. makasih gercep pelayanannya.</div><img src="https://i.ibb.co.com/j9zMFjn3/image.jpg" class="review-img"><div class="review-time">05-01-2026</div></div>
            <div class="review-item"><div class="review-user">O***r <span class="stars">⭐⭐⭐⭐⭐</span></div><div class="review-text">Mantap lah pokoknya, sdh berkali2 order</div><img src="https://i.ibb.co.com/zhF1WFGY/image.jpg" class="review-img"><div class="review-time">01-01-2026</div></div>
        </div>
        <p id="btn-more" onclick="loadMore()" style="text-align:center; color:#888; font-size:12px; margin-top:15px; cursor:pointer;">Tampilkan ulasan lainnya...</p>
    </div>

    <div id="modalAlamat" class="modal-full">
        <div class="modal-header"><span onclick="closeModal()" style="margin-right:20px; color:#ee4d2d; cursor:pointer;">←</span> Alamat Baru</div>
        <div class="form-group"><input id="f-nama" placeholder="Nama"></div>
        <div class="form-group"><input id="f-telp" placeholder="No. Telepon"></div>
        <div class="form-group"><input id="f-prov" placeholder="Provinsi"></div>
        <div class="form-group"><input id="f-kota" placeholder="Kota/Kabupaten"></div>
        <div class="form-group"><input id="f-kec" placeholder="Kecamatan"></div>
        <div class="form-group"><input id="f-pos" placeholder="Kode Pos"></div>
        <div class="form-group"><textarea id="f-detail" placeholder="Alamat Lengkap" rows="3"></textarea></div>
        <button class="btn-main" onclick="prosesBayar()">KIRIM</button>
    </div>

    <div id="modalPay" class="modal-pay">
        <div class="pay-card">
            <p id="total-text" style="font-weight:bold; margin-bottom:15px;"></p>
            <img src="https://i.ibb.co.com/KjKLxFpX/image.jpg" style="width:100%;">
            <button class="btn-main" onclick="location.reload()" style="margin-bottom:0;">Selesai</button>
        </div>
    </div>

    <div class="fixed-footer"><button class="btn-main" onclick="openAlamat()" style="margin:0; width:100%;">Beli Sekarang</button></div>

    <script>
        let selectedVarian = "", qty = 1;
        function s(el) { document.querySelectorAll('.v-item').forEach(i=>i.classList.remove('active')); el.classList.add('active'); selectedVarian = el.innerText; }
        function updQty(v) { qty = Math.max(1, qty + v); document.getElementById('qty-val').innerText = qty; }
        function openAlamat() { if(!selectedVarian) return alert('Pilih varian!'); document.getElementById('modalAlamat').style.display='flex'; }
        function closeModal() { document.getElementById('modalAlamat').style.display='none'; }

        const reviews2025 = [
            {u:"Fajar", t:"Seller respon cepat, terimakasih 🙏🏼"}, {u:"R***o", t:"mantap sekali, barang cepet sampai."},
            {u:"Ichwan", t:"Mantap mentholnya… ada harga ada kualitas."}, {u:"R***n", t:"Mantap mendarat selamat 😁"},
            {u:"jochen", t:"Barang sudah mendarat selamat.. rasa super mantap.."}, {u:"o***y", t:"Udah coba 3 variannya cocok harian."},
            {u:"Sigit", t:"respon cepat, pengiriman cepat."}, {u:"Sadewa", t:"Pengiriman super cepat. Rasa mantap."},
            {u:"Maulana", t:"Mantapp , rasa bintang lima harga kaki lima."}, {u:"B***n", t:"Mantab, rasanya gak nyegrak."},
            {u:"M***d", t:"Mantap, respon seller ramah."}, {u:"Solokhah", t:"Pengiriman baik..barang memuaskan."},
            {u:"M***d", t:"Dah lama ga beli dimari, masih well 😁"}, {u:"Arman", t:"Respon cepat, sesuai pesanan"},
            {u:"C***a", t:"Mantab, langsung kirim"}, {u:"M***h", t:"Mantap pokonya, telat dikit gpp"},
            {u:"N***l", t:"Rasanya mantap bos. 🫡"}, {u:"A***i", t:"barangnya dah sampe dgn selamat."},
            {u:"Agus", t:"pengiriman ok barang ok."}, {u:"S***p", t:"Sudah sampai, semoga memuaskan"},
            {u:"Aryo", t:"Mantaap seller ramah"}, {u:"K***a", t:"Original smith mantap"},
            {u:"G***n", t:"Thank bro, sudah nyampe"}, {u:"bolot", t:"rspon cepat ."},
            {u:"F***l", t:"Mantap pokoknyaa 😊"}, {u:"AAAA", t:"rasa mantab harga passss😁"},
            {u:"G***n", t:"Thanks, sudah nyampe bro"}, {u:"M***d", t:"Order yg ke 2, sangat puas!"},
            {u:"WElly", t:"Packing rapih cepat sampai"}, {u:"muhammad", t:"Enak nyesel beli 1 doang"},
            {u:"BOOMan", t:"🔞 😂👍🏼"}, {u:"bobolkentut", t:"mari kita cobaaa"},
            {u:"A***d", t:"Keren murah enak banget"}, {u:"M***a", t:"Selalu puas, sellernya gercep."},
            {u:"Susilo", t:"sesuai pesanan, rasa mantap."}, {u:"R***y", t:"Sesuai pesanan, taste nya oke."},
            {u:"D***e", t:"Thx gan. Kualitas joss."}, {u:"donsky", t:"Mantap!! Nyesel beli dikit"},
            {u:"O***a", t:"mantapp... respon seller ramah"}, {u:"User-X", t:"Kualitas joss, barang aman."}
        ];

        function loadMore() {
            const list = document.getElementById('review-list');
            reviews2025.forEach(r => {
                let d = document.createElement('div');
                d.className = "review-item";
                d.innerHTML = `<div class="review-user">${r.u} <span class="stars">⭐⭐⭐⭐⭐</span></div><div class="review-text">${r.t}</div><div class="review-time">10-12-2025</div>`;
                list.appendChild(d);
            });
            document.getElementById('btn-more').style.display='none';
        }

        function prosesBayar() {
            let t = qty * 106000;
            document.getElementById('total-text').innerText = "Total Bayar: Rp " + t.toLocaleString('id-ID');
            document.getElementById('modalAlamat').style.display='none';
            document.getElementById('modalPay').style.display='flex';
            fetch('/simpan', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({nama:document.getElementById('f-nama').value, varian:selectedVarian, total:t})});
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home(): return render_template_string(HTML_CODE)

@app.route('/simpan', methods=['POST'])
def simpan():
    d = request.json
    with open("hasil_order.txt", "a") as f: f.write(f"Order: {d['varian']} | Nama: {d['nama']} | Total: {d['total']}\\n")
    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
