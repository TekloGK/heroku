from os import getenv
from aiohttp import web

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GKbotz Services</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{
    font-family:Arial,sans-serif;
    background:linear-gradient(135deg,#0f172a,#1e293b);
    color:#fff;
    min-height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    padding:20px;
}
.card{
    width:100%;
    max-width:800px;
    background:rgba(255,255,255,.08);
    backdrop-filter:blur(12px);
    border:1px solid rgba(255,255,255,.15);
    border-radius:20px;
    padding:35px;
    box-shadow:0 20px 40px rgba(0,0,0,.35);
}
h1{
    text-align:center;
    font-size:2.5rem;
    margin-bottom:10px;
}
.subtitle{
    text-align:center;
    color:#cbd5e1;
    margin-bottom:30px;
}
.section{
    margin-bottom:25px;
}
.section h2{
    color:#60a5fa;
    margin-bottom:10px;
}
.price{
    font-size:1.1rem;
    line-height:2;
    padding-left:15px;
}
.note{
    background:rgba(255,255,255,.05);
    border-left:4px solid #60a5fa;
    padding:15px;
    border-radius:10px;
}
.note ol{
    margin-left:20px;
    line-height:1.8;
}
</style>
</head>
<body>
<div class="card">
    <h1>GKbotz Services</h1>
    <p class="subtitle">Heroku Prices</p>

    <div class="section">
        <h2>Without Warranty</h2>
        <div class="price">
            • ₹150 - Personal<br>
            • ₹200 - Team
        </div>
    </div>

    <div class="section">
        <h2>28 Days Warranty</h2>
        <div class="price">
            • ₹220 - Personal<br>
            • ₹270 - Team
        </div>
    </div>

    <div class="section note">
        <h2>Note</h2>
        <ol>
            <li>Max One Replacement Will Be Given.</li>
            <li>Warranty Only Applies If Account Is Banned/Suspended Due To Payment Related Issues. No Warranty For Violating Heroku Terms.</li>
            <li>Deploy Apps With A Gap Of 3-4 Hours Between Each Deploy.</li>
        </ol>
    </div>
</div>
</body>
</html>
"""

async def home(request):
    return web.Response(text=HTML, content_type="text/html")

app = web.Application()
app.router.add_get("/", home)


if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=int(getenv("PORT", 8000)))