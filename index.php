<?php
    session_start();
    $_SESSION['nonce'] = substr(str_shuffle(MD5(microtime())), 0, 10);
?>
<!DOCYTPE html>
<html>
    <head>
        <title>Sadoos Demo</title>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <link rel="stylesheet" href="main.css">
    </head>
    <body style="background-image: url(bg.png);"><div class="center">
        <input type="button" class="btn button-64" style="margin-top:50%; margin-left:40%" value="برای ضبط نگه دارید" />
        <a href="https://demo.sadoos.ir/Sadoos/p.php" class="button-64">دیدن نتایج</a>
        </div>
        <script type="text/javascript">
            window.nonce = "<?php echo $_SESSION['nonce']; ?>"
            // courtesy https://medium.com/@bryanjenningz/how-to-record-and-play-audio-in-javascript-faa1b2b3e49b
            const recordAudio = () => {
              return new Promise(async resolve => {
                const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                const mediaRecorder = new MediaRecorder(stream);
                const audioChunks = [];

                mediaRecorder.addEventListener("dataavailable", event => {
                  audioChunks.push(event.data);
                });

                const start = () => mediaRecorder.start();

                const stop = () =>
                  new Promise(resolve => {
                    mediaRecorder.addEventListener("stop", () => {
                      const audioBlob = new Blob(audioChunks);
                      const audioUrl = URL.createObjectURL(audioBlob);
                      const audio = new Audio(audioUrl);
                      const play = () => audio.play();
                      resolve({ audioBlob, audioUrl, play });
                    });

                    mediaRecorder.stop();
                  });

                resolve({ start, stop });
              });
            }

            /* simple timeout */
            const sleep = time => new Promise(resolve => setTimeout(resolve, time));

            /* init */
            (async () => {
                const btn = document.querySelector("input");
                const recorder = await recordAudio();
                let audio; // filled in end cb

                const recStart = e => {
                    recorder.start();
                    btn.initialValue = btn.value;
                    btn.value = "در حال ضبط...";
                }
                const recEnd = async e => {
                    btn.value = btn.initialValue;
                    audio = await recorder.stop();
                    audio.play();
                    uploadAudio(audio.audioBlob);
                }

                const uploadAudio = a => {
                    if (a.size > (10 * Math.pow(1024, 2))) {
                        document.body.innerHTML += "Too big; could not upload";
                        return;
                    }
                    const f = new FormData();
                    f.append("nonce", window.nonce);
                    f.append("payload", a);

                    fetch("save_audio.php", {
                        method: "POST",
                        body: f
                    })
                    // .then(_ => {
                    //     document.body.innerHTML += `
                    //         <br/> <a href="audio.wav">saved; click here</a>
                    //     `
                    // });
                }


                btn.addEventListener("mousedown", recStart);
                btn.addEventListener("touchstart", recStart);
                window.addEventListener("mouseup", recEnd);
                window.addEventListener("touchend", recEnd);
            })();
        </script>
    </body>
</html>

