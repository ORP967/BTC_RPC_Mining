# BTC_RPC_Mining
Use your own Bitcoin Core to CPU mine bitcoins using python3.

I changed  Avatar Vanya Sergeev's code (https://github.com/vsergeev/ntgbtminer) to be constantly looking for a new block every 20 seconds or so. If a new block is detected, it downloads a new block template and starts all over again. Currently getting 1.01KH/s.

If anyone can help shorten the code and make it faster would be greatly appreciated.

To run this program, you'll need to add the lines found on bitcoin.conf to your bitcoin core system and reindex it if you haven't done so yet.

To open the bitcoin.conf file run bitcoin core, go to Settings > Options and click the "Open Configuration File" button. Press OK button. Copy and paste the lines on the bitcoin.conf file I have written onto your file, press the Save button and close the window.

To reindex- 
When you start bitcoin core add the command -reindex. Example: If your bitcoin core was installed in the /usr/local/bin folder, you would start it like this:
/usr/local/bin/bitcoin-qt -reindex

This will take a very long time to complete. Currently it is taking me about 5 days to complete.

Once you are comfortable playing with the program, change the rpcuser name and rpcpassword for security reasons. But for now you can leave it like it is in the files to get started playing with the program
