const e =require('crypto-js')
// 加密shouquan.php参数,用这个key: dvyYRQlnPRCMdQSe 
// 解密m3u8用这个key: 36606EE9A59DDCE2 

const decrypt = function (text,key, iv) {
  return e.AES.decrypt(text, 
  e.enc.Latin1.parse(key), {
   iv:e.enc.Latin1.parse(iv),
   mode: e.mode.CBC,
   padding: e.pad.NoPadding,
  }).toString(e.enc.Utf8)
 }

const encrypt = function (text,key, iv) {

    return e.AES.encrypt(text, e.enc.Latin1.parse(key), {
      iv:e.enc.Latin1.parse(iv),
      mode: e.mode.CBC,
      padding: e.pad.Pkcs7
    }).toString()
  }


// "m3u8.okjx.cc|c98851835f93fa6f"
// console.log(encrypt('m3u8.okjx.cc|c98851835f93fa6f'
// ,"dvyYRQlnPRCMdQSe"
// ,"c98851835f93fa6f"))

console.log(decrypt("hFsaNOHoCwp4I3+MicxRQTLiyeIwIALznU6YEuLcAmFyts3Yt9IfHc/JY94i4NVzyXMCfL2gaW88KskGpnUPl35HcLzMZJfohnaiu5/m/6ObssUfugjS/0UlGgcOJsb5ZFptWNFXuLJQzvyZc5WD9t/Zf/yRynRBdSHG4GMN2+fcGCsiP5uhm2ZYrx0UTjL1KwpryPim8jPMNztj+h6ehwQmqAiRCohtOsssw40csh++yqQJqXECiiJ/9mmcI0Fe"
,"36606EE9A59DDCE2"
,"057f1eed099f2f7e"))




