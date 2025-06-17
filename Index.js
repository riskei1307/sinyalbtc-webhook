const express = require('express')
const axios = require('axios')

const BOT_TOKEN = process.env.BOT_TOKEN
const CHAT_ID = process.env.CHAT_ID
const TELEGRAM_API = `https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`

const app = express()
app.use(express.json())

app.get('/send', async (req, res) => {
  const message = req.query.message || '⚠️ Tes sinyal dari Railway!'
  try {
    await axios.post(TELEGRAM_API, {
      chat_id: CHAT_ID,
      text: message,
      parse_mode: 'Markdown'
    })
    res.send('Pesan terkirim ✔️')
  } catch (err) {
    console.error(err)
    res.status(500).send('Gagal kirim pesan')
  }
})

const PORT = process.env.PORT || 3000
app.listen(PORT, () => console.log(`Server berjalan di port ${PORT}`))
