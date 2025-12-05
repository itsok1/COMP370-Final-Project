import csv
import pandas as pd
from io import StringIO

# 你的原始 CSV 文本粘贴在这里
csv_text_ap = """ 
"Yesterday","Zelenskyy visits Picasso’s ‘Guernica’ painting after drawing parallel to Ukraine’s bombing","Ukraine’s President Volodymyr Zelenskyy visited Spain and stopped to see Pablo Picasso’s “Guernica” in Madrid.","https://apnews.com/article/zelenskyy-ukraine-spain-russia-war-ed58ec3cd0d7995b9e9dff3090a30076"

"November 16","Greece and Ukraine sign a US gas supply deal as Zelenskyy visits Athens","An agreement to supply Ukraine with U.S. liquefied natural gas has been signed in Athens during Ukrainian President Volodymyr Zelenskyy’s visit to Greece.","https://apnews.com/article/lng-us-energy-ukraine-greece-deal-gas-f749e45a3cbea1de6fe664f9a09631f6"

"Yesterday","Zelenskyy will visit Turkey in a new bid to jump-start talks to end Russia’s invasion","Ukrainian President Volodymyr Zelenskyy plans to visit Turkey this week to revive talks on ending Russia’s invasion, which began nearly four years ago.","https://apnews.com/article/russia-ukraine-war-turkey-negotiations-spain-france-6a739b523cb926d92f2bf44b24dfc3c3"

"November 10","Zelenskyy seeks Patriot systems from US to counter Russia’s power grid attacks","President Volodymyr Zelenskyy says he wants to order 25 Patriot air defense systems from the United States as Ukraine tries to fend off relentless Russian aerial attacks.","https://apnews.com/article/russia-ukraine-war-power-patriots-drones-missiles-d954d3ad6a3b6c91dbb1d86f886843d5"

"October 13","Zelenskyy to visit Washington this week seeking long-range weapons and a Trump meeting","Ukrainian President Volodymyr Zelenskyy says he will travel to the United States this week for talks on the potential U.S. provision of long-range weapons.","https://apnews.com/article/russia-ukraine-war-trump-zelenskyy-eu-5350381ba83ce1f53928ac435d4c4e7d"

"October 28","Ukraine’s long-range strikes cut Russia’s oil refining capacity by 20%, Zelenskyy says","Ukrainian President Volodymyr Zelenskyy says long-range strikes on Russian refineries have reduced Moscow’s oil refining capacity by 20%.","https://apnews.com/article/russia-ukraine-war-oil-refineries-zelenskyy-fa04014c6c1bdf0e15123d898c491b03"

"November 16","Zelenskyy says Ukraine is working on a prisoner exchange with Russia","Ukraine is working to resume prisoner exchanges with Russia that could bring home 1,200 Ukrainian prisoners.","https://apnews.com/article/ukraine-russia-prisoner-exchange-zelenskyy-istanbul-drones-b66ea7f9ad1ae4072861b732437b301a"

"October 16","Russian barrage causes blackouts in Ukraine as Zelenskyy seeks Trump’s help","Russia has launched a heavy bombardment on Ukraine’s energy facilities, using hundreds of drones and dozens of missiles.","https://apnews.com/article/russia-ukraine-war-trump-zelenskyy-visit-attacks-78c1b21fde3494786b0dfe0268c4a21e"

"October 9","Ukraine’s new missiles and drones cause gas shortages in Russia, Zelenskyy says","Ukraine’s new long-range missiles and drones are causing significant gas shortages in Russia.","https://apnews.com/article/russia-ukraine-war-zelenskyy-missiles-drones-4de5965f6716f9234f0c000da091eeeb"

"November 15","Once a shadowy dealmaker, former Zelenskyy associate is accused in Ukrainian corruption scandal","Tymur Mindich has been named as the mastermind behind a $100 million embezzlement scheme in Ukraine.","https://apnews.com/article/russia-ukraine-war-corruption-scandal-tymur-mindich-4b6940ca6521193fadfc263e4c6d51f4"

"October 14","Russian aerial attack hits a Ukrainian hospital, days before Zelenskyy meets Trump","Ukrainian President Volodymyr Zelenskyy says Russian forces launched powerful glide bombs and drones against Kharkiv.","https://apnews.com/article/russia-ukraine-zelenskyy-trump-tomahawks-a8ad84233358f7592fa11cda08e82610"

"October 25","Russian missile and drone attacks kill 4 in Ukraine as Zelenskyy pleads for air defense","Russian missile and drone attacks overnight killed at least four and wounded 20.","https://apnews.com/article/russia-ukraine-zelenskyy-missile-ballistic-kyiv-4381b48b931d7ed32e44a6d671b97dd5"

"2 hours ago","Russian attack kills 25 in Ukraine’s Ternopil as Zelenskyy meets Erdogan in Turkey","A Russian strike on Ternopil killed 25 people, including three children.","https://apnews.com/article/russia-ukraine-war-drone-missile-attack-a8c310e868905ea8905334ffb3869fcb"

"October 15","Ukrainian officials meet with US weapons manufacturers before Trump-Zelenskyy talks","A Ukrainian delegation met major American weapons manufacturers on a U.S. visit.","https://apnews.com/article/russia-ukraine-war-trump-zelenskyy-weapons-31e8d494c92300524a0f50cebff28f7d"

"October 3","Zelenskyy warns that Russian drones endanger Chernobyl and other nuclear plants in Ukraine","Russian attacks raise concerns about nuclear safety; a drone cut power at Chernobyl for 3 hours.","https://apnews.com/article/russia-ukraine-drones-chernobyl-nuclear-plant-c451827a8a842d634203c0111131d152"

"October 18","Ukrainians disappointed after Trump-Zelenskyy meeting fails to immediately secure Tomahawk missiles","Ukrainians express disappointment as US may not provide long-range Tomahawks.","https://apnews.com/article/russia-ukraine-war-zaporizhzhia-62250a9b0c6c23a919b31780b2c3adbc"

"August 29","Zelenskyy seeks talks with Trump and European leaders on slow progress of peace efforts with Russia","Zelenskyy says Ukraine wants meetings with Trump and EU leaders to discuss peace talks.","https://apnews.com/article/russia-ukraine-kyiv-attack-putin-trump-47e0fa10cded79063cf8cb9db7a2bcb7"

"October 24","Ukraine’s Zelenskyy urges US to broaden Russian oil sanctions and seeks long-range missiles","Zelenskyy urges US to expand sanctions on Russia’s oil sector.","https://apnews.com/article/russia-ukraine-war-london-coalition-willing-2a9e4d936356533821175e420e8a0a2f"

"August 17","European leaders to join Ukraine’s Zelenskyy for meeting with Trump","European and NATO leaders will join Zelenskyy in Washington for talks with Trump.","https://apnews.com/article/european-leaders-white-house-meeting-zelenskyy-trump-d7b082bae4136ef8932e16ac2d166303"

"August 18","Back in the Oval Office, Zelenskyy wears a blazer and Trump doesn’t shout","Zelenskyy and Trump meet again in the Oval Office with a notably calmer tone.","https://apnews.com/article/zelenskyy-trump-blazer-white-house-russia-ukraine-war-81ce5677450d039552aa12e134739da6"

"September 16","Zelenskyy calls for a European air defense system as Russian strike wounds 20","Russian bombardment on Zaporizhzhia wounded 20 people including children.","https://apnews.com/article/russia-ukraine-war-zelenskyy-trump-3147203ffd293b9518655f910711d801"

"August 19","Zelenskyy deploys gratitude diplomacy for second visit to Oval Office","Zelenskyy expresses strong gratitude toward Trump during Oval Office meeting.","https://apnews.com/article/thank-you-diplomacy-trump-zelenskyy-russia-ukraine-d2f4ce2a0a27f81dba8ea07f5fb1bfd3"

"November 17","Ukraine plans to buy up to 100 Rafale warplanes and air defense systems from France","Ukraine intends to buy up to 100 Rafale jets plus air-defense systems from France.","https://apnews.com/article/france-ukraine-warplanes-rafale-1ac56c0377a9d40fd28462df1b1acd63"

"August 31","Zelenskyy announces arrest in shooting death of pro-Western Ukrainian politician Andriy Parubiy","Ukraine arrests a suspect in the killing of former parliament speaker Parubiy.","https://apnews.com/article/ukraine-parubiy-killed-lviv-3f322375d0a7c694bd0909018ceb0382"

"September 3","Russia launches over 500 drones and missiles at Ukraine as Zelenskyy seeks more support","Russia launched over 500 drones and missiles at Ukrainian infrastructure.","https://apnews.com/article/russia-ukraine-war-trump-zelenskyy-putin-9d6b9bf76a15971c17ae2de9ca1211b5"

"October 31","Russia deploys 170,000 troops for push in Ukraine’s Donetsk region, Zelenskyy says","Russia has deployed 170,000 troops in Donetsk aiming to seize Pokrovsk.","https://apnews.com/article/russia-ukraine-war-missile-united-nations-4624a6463aa3637e2d47baec9c5edcbe"

"September 22","Russia and Ukraine trade deadly drone strikes as Zelenskyy anticipates intense diplomacy at UN","Russia and Ukraine trade deadly drone strikes as UN diplomacy intensifies.","https://apnews.com/article/russia-ukraine-war-united-nations-zelenskyy-trump-58e26bfcc00f523c0e62b15b361f7ee0"

"August 8","Controversy over corruption law shows the limits of Ukrainian goodwill toward Zelenskyy","Zelenskyy reverses a controversial law after mass protests challenge his leadership.","https://apnews.com/article/russia-ukraine-war-corruption-law-trust-zelenskyy-66bd83681bb6df4ac9fe8335ede9385a"

"September 21","Ukrainian and Russian attacks kill 3 civilians as Zelenskyy prepares to meet Trump","Cross-border attacks kill three people as Zelenskyy prepares for Trump meeting.","https://apnews.com/article/russia-ukraine-war-belgorod-drones-7aedb2a342e56dd22504448d1ccd1bed"

"August 12","Zelenskyy says Putin wants the rest of Ukraine’s Donetsk region as part of a ceasefire","Putin wants Ukraine to withdraw from remaining 30% of Donetsk, Zelenskyy says.","https://apnews.com/article/europe-trump-putin-summit-ukraine-territory-ba56ddbd24d1b7e8e0aca7754d0f180a"
"August 9","Zelenskyy rejects formally ceding Ukrainian territory, says Kyiv must be part of any negotiations","Ukrainian President Volodymyr Zelenskyy has rejected the idea of giving up land to end the war with Russia.","https://apnews.com/article/russia-ukraine-war-putin-trump-summit-zelenskyy-a01a6dbae85b10cc710c48f1558c1401"

"October 17","After Zelenskyy meeting, Trump calls on Ukraine and Russia to ‘stop where they are’ and end the war","President Donald Trump is calling on Kyiv and Moscow to “stop where they are” and end their brutal war.","https://apnews.com/article/trump-zelenskyy-putin-ukraine-tomahawks-ce697e5eda6ce9793b4343499d105a8c"

"September 17","Ukraine expects $3.5 billion fund for US weapons to sustain fight against Russia, Zelenskyy says","Ukraine expects to have a $3.5 billion fund by next month to buy weapons from the U.S. and sustain its defense.","https://apnews.com/article/russia-ukraine-war-us-weapons-minerals-86894a9ce6c86cede42d1adca8569d5e"

"September 30","Ukraine begins sharing drone expertise with Denmark deployment, Zelenskyy says","Ukraine is sharing drone-defense expertise with Denmark through joint exercises.","https://apnews.com/article/russia-ukraine-war-drones-europe-f15530ce5c47dbba26c334147e684471"

"August 18","Takeaways from Trump’s meeting with Zelenskyy and Europeans: Praise, security talks, more meetings","President Donald Trump says the U.S. could support a European force in Ukraine to maintain lasting peace.","https://apnews.com/article/russia-ukraine-war-trump-zelensky-what-to-know-f70e7c231251f263a66772d954eefff5"

"October 16","Zelenskyy arrives in the US ahead of his meeting with Trump","Ukrainian President Volodymyr Zelenskyy arrived in the U.S. ahead of his meeting with President Trump.","https://apnews.com/video/ukraine-president-zelenskyy-arrives-in-the-us-ahead-of-his-meeting-with-trump-8dc38d9658954e97abf8fa63215e2217"

"November 9","Zelenskyy calls for more sanctions against Russia after Dnipro apartment block strike","Zelenskyy demanded tougher sanctions after a deadly Russian strike on a Dnipro apartment block.","https://apnews.com/video/zelenskyy-calls-for-more-sanctions-against-russia-after-dnipro-apartment-block-strike-3ad2cf29682742d3a3f3e41f459e4045"

"October 1","Zelenskyy and UN atomic agency head warn of heightened risk at huge Ukrainian nuclear plant","Ukraine and the UN nuclear agency warn of rising risks at the occupied Zaporizhzhia plant.","https://apnews.com/article/russia-ukraine-war-zaporizhzhia-nuclear-plant-85e5b1512918d7293702429b808483bc"

"August 18","Trump begins planning for Putin-Zelenskyy meeting while affirming US help with security guarantees","Trump says he is arranging a meeting between Putin and Zelenskyy to work toward ending the war.","https://apnews.com/article/trump-putin-zelenskyy-russia-ukraine-war-d0ad768453210db23fe4b108f7b87135"

"July 23","Zelenskyy faces backlash as Ukrainians protest new anti-corruption law","Ukrainians protest a new law they say weakens anti-corruption institutions.","https://apnews.com/article/russia-ukraine-war-corruption-protests-zelenskyy-talks-fb2fdeb3fbf36a37b2e1eefb385bac87"

"October 16","Trump says he’ll meet with Putin in Hungary. He first meets Friday with Zelenskyy at the White House","Trump plans to meet Zelenskyy before a scheduled sit-down with Putin.","https://apnews.com/article/trump-zelenskyy-putin-russia-ukraine-e3a1d62d2a24f459aa6dbbfa940e1067"

"November 14","Zelenskyy says deadly Russian drone attack on Kyiv “must not go unpunished”","Zelenskyy demands accountability after a major Russian attack on Kyiv.","https://apnews.com/video/zelenskyy-says-deadly-russian-drone-attack-on-kyiv-must-go-unpunished-092b0a0f0bda4fea96d50d2091f40262"

"August 19","Sen. Lindsey Graham says Trump ready to ‘crush’ Russian economy if Putin avoids talks with Zelenskyy","Graham says Trump will impose harsh sanctions if Putin refuses peace talks with Zelenskyy.","https://apnews.com/article/russia-sanctions-ukraine-trump-zelenskyy-war-negotiations-d94711651ab5b96f7b771c1fb3af1179"

"January 10","Zelenskyy meets US Defence Secretary Austin in Germany","Zelenskyy and Austin urge continued U.S. military support for Ukraine.","https://apnews.com/video/lloyd-austin-volodymyr-zelenskyy-ukraine-government-vladimir-putin-austin-zelenskyy-a563dac1eb044541a599754b03b9c4b3"

"October 17","Zelenskyy says Trump now has ‘momentum’ to stop Russia-Ukraine war","Zelenskyy says Trump now has momentum needed to help end the war.","https://apnews.com/video/zelenskyy-says-trump-now-has-momentum-to-stop-russia-ukraine-war-a1b5e62d58634e3a8a91f9b84f3f4cb3"

"October 23","Zelenskyy meets with Macron, Merz and other EU leaders on sidelines of Brussels summit","Zelenskyy held several bilateral meetings at the EU summit in Brussels.","https://apnews.com/video/zelenskyy-meets-with-macron-merz-and-other-eu-leaders-on-sidelines-of-brussels-summit-5912b79ebfd5401c88684c87dcad3fc0"

"October 24","Zelenskyy meets King Charles at Windsor Castle","Zelenskyy met King Charles to discuss European security commitments.","https://apnews.com/video/zelenskyy-meets-king-charles-at-windsor-castle-0dde6a5ab14f4af7ae7c26a274bd11d7"

"September 23","Zelenskyy laments Security Council inaction over Russian aggression","Zelenskyy criticizes UN inaction as Russia escalates attacks.","https://apnews.com/video/zelenskyy-laments-security-council-inaction-over-russian-aggression-15f8f16a130f42a78c22fc0d7ecd0109"

"November 16","Greece and Ukraine sign a US gas supply deal as Zelenskyy visits Athens","Ukraine signs deal to import U.S. natural gas via Greece.","https://apnews.com/video/greece-and-ukraine-sign-a-us-gas-supply-deal-as-zelenskyy-visits-athens-f0f89f9f069d4dffafd8d1d030222174"

"2 hours ago","Ukrainian President Zelenskyy meets Turkish President Erdogan in Ankara in search of diplomatic support","Zelenskyy seeks Turkish diplomatic backing against Russia.","https://apnews.com/video/ukrainian-president-zelenskyy-meets-turkish-president-erdogan-in-ankara-in-search-of-diplomatic-support-5fb377274228407f8017940724779d33"

"August 18","Zelenskyy’s attire comes up for the second time in the Oval Office","Zelenskyy wears a suit on return to the White House after past criticism.","https://apnews.com/video/zelenskyys-attire-comes-up-for-the-second-time-in-the-oval-office-2fcb45aaf1d2470aadac6a742a897b0d"

"November 3","Ukraine gets more US-made air defense systems to counter deadly Russian attacks","Ukraine receives new Patriot systems to counter Russian strikes.","https://apnews.com/article/russia-ukraine-war-patriots-drones-missiles-facc290c820961f25cda6c7fd689baf3"

"September 28","Ukraine’s Zelenskyy accuses Russia of launching drones from shadow fleets","Zelenskyy says Russia is launching drones from covert ships.","https://apnews.com/video/ukraines-zelenskyy-accuses-russia-of-launching-drones-from-shadow-fleets-1724c00f27b142ce8cf059c8792ddcc6"

"October 14","Zelenskyy says there is ‘momentum’ for peace in Ukraine after Gaza ceasefire","Zelenskyy praises Trump’s role in securing Gaza ceasefire and sees momentum for peace.","https://apnews.com/video/zelenskyy-says-there-is-momentum-for-peace-in-ukraine-after-gaza-ceasefire-47a4f1f7a22a4bc1beae3ef2c665ef4a"

"July 9","Ukraine’s Zelenskyy meets with Pope Leo XIV. Both propose the Vatican as site for peace talks","Zelenskyy and Pope Leo XIV discuss Vatican-hosted peace talks.","https://apnews.com/article/vatican-pope-leo-zelenskyy-children-taken-ukraine-cb1437b87d9970d0642648152979fcd0"

"September 27","Ukraine nuclear plant enters fifth day on emergency power as Zelenskyy announces $90B arms deal","Zaporizhzhia nuclear plant remains on emergency power as Ukraine unveils major arms deal.","https://apnews.com/article/zaporizhzhia-nuclear-ukraine-russia-zelenskyy-92f0490b455ee7254fe2498874b23725"

"July 17","Zelenskyy appoints a new prime minister for a war-weary Ukraine","Zelenskyy appoints negotiator Yuliia Svyrydenko as new prime minister.","https://apnews.com/article/russia-ukraine-war-government-reshuffle-zelenskyy-svyrydenko-c64ec1fd2475ad85c6a54a50c63076eb"

"September 24","In his words: Trump’s rhetoric about Zelenskyy and Putin has evolved","Trump’s stance toward Zelenskyy and Putin has shifted over time.","https://apnews.com/article/trump-russia-ukraine-putin-comments-2b977a12e445817fffd6ef9f8df9aa38"

"July 24","Zelenskyy moves to restore independence of Ukraine anti-graft agencies after protests, EU criticism","Zelenskyy introduces a bill to restore anti-corruption agency independence.","https://apnews.com/article/russia-ukraine-war-corruption-protests-zelenskyy-law-6766134c963f0423d88c2ac1749f8c11"

"September 24","Ukraine’s president says the world is in ‘the most destructive arms race in human history’","Zelenskyy warns world leaders about global re-armament dangers.","https://apnews.com/article/ukraine-zelenskyy-unga-united-nations-russia-ce276671d255befeba10a324caf2a7e5"
"June 19","Zelenskyy calls for more pressure on Russia after deadly missile strike in Ukrainian capital Kyiv","Zelenskyy urges greater international pressure after a Russian missile strike killed 23 in Kyiv.","https://apnews.com/article/ukraine-zelenskyy-war-russia-missile-strike-91245843b6ef6f191313686458676b82"

"September 24","Macron and Zelenskyy hold bilateral meeting at the United Nations","Macron and Zelenskyy met on the sidelines of the UN General Assembly.","https://apnews.com/video/macron-and-zelensky-hold-bilateral-meeting-at-the-united-nations-d25c943c7c194a0eb1b0c65a9ffb20ee"

"August 19","Kyiv residents react to Zelenskyy-Trump meeting with optimism","Kyiv residents closely watched the Trump–Zelenskyy meetings and reacted positively.","https://apnews.com/video/kyiv-residents-react-to-zelenskyy-trump-meeting-with-optimism-d05c9323d0404a52975415e97f4d81cf"

"October 21","Zelenskyy reiterates the country’s readiness for ceasefire along the current frontlines","Zelenskyy says Ukraine is ready for a ceasefire along existing lines.","https://apnews.com/video/zelenskyy-reiterates-the-countrys-readiness-for-ceasefire-along-the-current-frontlines-e2634556a9f14ff2b0efb07386bc9056"

"August 7","Trump says he would meet with Putin even if the Russian leader won’t meet with Ukraine’s Zelenskyy","Trump says he would meet Putin even if Putin refuses to meet Zelenskyy.","https://apnews.com/article/russia-ukraine-war-poll-trump-sanctions-deadline-7cefb2df66f494f58a16b684a2c76687"

"August 24","Zelenskyy prays with first lady on Ukraine’s independence day","Zelenskyy joined a prayer service marking Ukraine’s 34th Independence Day.","https://apnews.com/video/zelenskyy-prays-with-first-lady-on-ukraines-independence-day-777128d7829245e695513d36619f39d5"

"October 3","Zelenskyy meets European leaders in Copenhagen at 7th European Political Community Summit","Zelenskyy met with several European leaders during the EPC summit.","https://apnews.com/video/zelenskyy-meets-european-leaders-in-copenhagen-at-7th-european-political-community-summit-5f36428095924e1d9d68b33812b5af72"

"September 23","Carney and Zelenskyy push for the return of abducted Ukrainian children","Zelenskyy and PM Carney urged stronger global action to return abducted Ukrainian children.","https://apnews.com/video/carney-and-zelenskyy-push-for-the-return-of-abducted-ukrainian-children-fbd1beb96f9a4b0cbb17156d1385540c"

"October 16","Zelenskyy arrives in US to meet with Trump","Zelenskyy arrived in the U.S. for talks on long-range weapons.","https://apnews.com/video/zelenskyy-arrives-in-us-to-meet-with-trump-492c6dfe49a34c69a0f68d443bca0111"

"July 22","Thousands gather to protest as Zelenskyy signs bill weakening anti-corruption agencies","Thousands protested after Zelenskyy signed a controversial anti-corruption law.","https://apnews.com/article/ukraine-corruption-law-european-union-f1ab949db19e079a52291c020ec3d24e"

"June 26","Zelenskyy approves plans on special tribunal to prosecute Russian leaders over Ukraine","Ukraine approved plans for a special tribunal to prosecute Russian leadership.","https://apnews.com/article/ukraine-russia-tribunal-zelenskyy-eaa224303d17a52e73c954b6ce612aae"

"October 22","Zelenskyy and Kristersson watch Swedish fighter jets perform as countries agree deal on Gripen planes","Zelenskyy and Sweden showcased fighter jets in a Gripen cooperation deal.","https://apnews.com/video/zelenskyy-and-kristersson-watch-swedish-fighter-jets-perform-as-countries-agree-deal-on-gripen-planes-9e719bb2d70b483e8ef80b45fd9e5fb9"

"October 17","Trump hosts Zelenskyy at the White House as Ukraine pushes for Tomahawk missiles","Zelenskyy pressed the U.S. for Tomahawk missiles during a White House meeting.","https://apnews.com/video/trump-hosts-zelenskyy-at-the-white-house-as-ukraine-pushes-for-tomahawk-missiles-4ba52ee2469a487f9850035af8abdf4d"

"November 13","EU renews demand that Ukraine crack down on corruption in wake of major energy scandal","EU officials pressured Ukraine to intensify anti-corruption efforts.","https://apnews.com/article/russia-ukraine-war-corruption-scandal-pokrovsk-a25b76c6c9830baafcf16ac5648bdd4c"

"2 hours ago","Ukraine asks Vatican to formalize mediation role for return of citizens taken by Russia","Ukraine urged the Vatican to formalize its mediation role in returning abducted citizens.","https://apnews.com/article/vatican-ukraine-russia-war-negotiations-children-c83dc48e3c197a66bb1377bbb50a341a"

"October 17","Trump and Zelenskyy meet at the White House as Ukraine seeks Tomahawk missiles","Trump met Zelenskyy at the White House; the U.S. remains hesitant on Tomahawks.","https://apnews.com/video/trump-and-zelenskyy-meet-at-the-white-house-as-ukraine-seeks-tomahawk-missiles-2e2bab183eb643a9927eec150eb35a19"

"October 17","Zelenskyy meets representatives of defense companies and energy sector during US visit","Zelenskyy thanked Raytheon for Patriot support during U.S. meetings.","https://apnews.com/video/zelenskyy-meets-representatives-of-defense-companies-and-energy-sector-during-us-visit-cebb60a5a4ce452b87ad2ba469acc6d3"

"July 17","Ukraine to boost domestic arms production to counter Russia’s invasion, says Zelenskyy","Ukraine aims to meet half its military needs with domestic production within months.","https://apnews.com/article/russia-ukraine-war-weapons-patriots-zelenskyy-146ada6ec9ee16d23fc9a6ef1a8039ef"

"September 23","Zelenskyy holds a meeting with the President of Switzerland Karin Keller-Sutter on the sidelines of UNGA","Zelenskyy met Switzerland’s president during the UNGA.","https://apnews.com/video/zelenskyy-holds-a-meeting-with-the-president-of-switzerland-karin-kellersutter-on-the-sidelines-of-unga-80faba9a6f3b49ae81ce9dfab0e8f3b0"

"September 24","In his words: Trump’s rhetoric about Zelenskyy and Putin has evolved","Trump’s stance toward Zelenskyy and Putin has shifted since taking office.","https://apnews.com/video/in-his-words-trumps-rhetoric-about-zelenskyy-and-putin-has-evolved-6bfef50874864f0da5214d6cbc25e7e1"

"August 18","Zelenskyy arrives at White House, meeting with Trump and European leaders.","Zelenskyy was welcomed at the West Wing by Trump ahead of meetings.","https://apnews.com/video/zelenskyy-arrives-at-white-house-meeting-with-trump-and-european-leaders-77855e091de942028c277d8c622471a1"

"June 14","Zelenskyy warns oil price surge could help Russia’s war effort","Zelenskyy says higher global oil prices will increase Russia’s wartime income.","https://apnews.com/article/russia-ukraine-war-iran-israel-zelenskyy-ba2a52ce82897f16f76f52d4b8e53b34"

"October 16","Expert says Russia-Ukraine war ceasefire ‘unlikely’ as Trump set to meet Zelenskyy","Analysts say a ceasefire remains unlikely before Trump–Zelenskyy talks.","https://apnews.com/video/expert-says-russia-ukraine-war-ceasefire-unlikely-as-trump-set-to-meet-zelenskyy-5004e56b78bc449b9d8950ba6ef5ca6b"

"3 hours ago","Top Ukrainian ministers submit their resignations as the country is rocked by a corruption scandal","Ukraine’s justice and energy ministers resigned amid a major corruption scandal.","https://apnews.com/article/russia-ukraine-war-corruption-scandal-6e33b63b8071f46140956d4d23ab00de"

"5 hours ago","Poland plans to charge 2 Ukrainians with sabotage of terrorist nature for railway explosion","Poland plans to prosecute two Ukrainians over a train-track explosion.","https://apnews.com/article/poland-railway-sabotage-ukraine-russia-consulate-gdansk-475619da2228aee03bfe90e75565f229"

"Yesterday","Drone strikes Turkish tanker in Ukraine’s Odesa, where US natural gas will go","A drone hit a Turkish tanker carrying gas via the Odesa region.","https://apnews.com/article/russia-ukraine-war-tanker-drone-fire-ea4ef368e58ef0936d24b27cd56073af"

"May 13","Zelenskyy says he will be waiting for Putin in Ankara for talks","Zelenskyy says he is ready to meet Putin in Ankara to negotiate an end to the war.","https://apnews.com/article/russia-ukraine-war-putin-zelenskyy-istanbul-b4a256f946ce892d6b2a7dfb0f3fba5b"

"October 20","Trump says he’s doubtful Ukraine can win the war with Russia as he prepares for Putin meeting","Trump says Ukraine may not be able to win the war.","https://apnews.com/article/russia-ukraine-war-zelenskyy-trump-tomahawk-fd61aa7ed980d2fe111f0521073b5382"

"June 21","Ukraine received at least 20 bodies of Russian soldiers in recent exchanges, Zelenskyy says","Ukraine received at least 20 Russian bodies in recent exchanges.","https://apnews.com/article/russia-ukraine-war-dead-soldiers-zelenskyy-3fe949eb4f050e6ef53b8eae7da0ef6c"

"July 22","Zelenskyy renews offer to meet with Putin as officials say Russian attacks kill a child in Ukraine","Zelenskyy renewed his offer for direct talks with Putin.","https://apnews.com/article/russia-ukraine-war-drones-peace-talks-a430896831b7bf527d36bf036c02c460"
"October 24","Starmer and Zelenskyy deliver statements during Coalition of the Willing meeting in London","Keir Starmer and Volodymyr Zelenskyy delivered statements after a “Coalition of the Willing” meeting in London.","https://apnews.com/video/starmer-and-zelenskyy-deliver-statements-during-coalition-of-the-willing-meeting-in-london-8c6fca5d25634a4a93af62e85bef15ea"

"November 11","Ukraine detains 5 people in $100M energy sector graft investigation","Ukraine's anti-corruption agency detained five people and identified seven others in a major graft case.","https://apnews.com/article/russia-ukraine-war-corruption-nuclear-energy-ef1839d090f7c96e4716c0299ed587fa"

"November 14","Russian drone and missile attack on Kyiv kills 6 people and injures at least 35","Russia launched a major missile/drone attack on Kyiv killing six and wounding at least 35.","https://apnews.com/article/war-russia-ukraine-energy-strikes-bombs-e0016ce1cec36f650e384a255250bf18"

"September 17","Iran executes man for alleged spying for Israel; activists say he was tortured into false confession","Iran executed a man accused of spying for Israel, but activists say he was tortured into a false confession.","https://apnews.com/article/iran-execution-israel-russia-ukraine-zelenskyy-a5d3e51eff55a449a11f254d909f1a70"

"August 19","Zelenskyy thanks Trump multiple times during meeting","Zelenskyy repeatedly thanked Trump during their meeting after past criticism from J.D. Vance.","https://apnews.com/video/zelenskyy-thanks-trump-multiple-times-during-meeting-a92f99b6805e4513b349ad5200784726"

"September 24","Zelenskyy to the UN: ‘We are now living through the most destructive arms race in history’","Zelenskyy warned world leaders about a dangerous global arms race.","https://apnews.com/video/zelenskyy-to-the-un-we-are-now-living-through-the-most-destructive-arms-race-in-history-9288b49fd3fd488582e780abf4ff1f2d"

"August 23","Zelenskyy takes part in ceremony marking Ukraine’s national flag day","Zelenskyy participated in a ceremony marking Ukraine’s national flag day in Kyiv.","https://apnews.com/video/zelenskyy-takes-part-in-ceremony-marking-ukraines-national-flag-day-6413fd1dad1e47d29361373fc163472a"

"June 25","Trump meets with Zelenskyy and says higher NATO defense spending may deter future Russian aggression","Trump said NATO defense spending increases may deter future Russian aggression.","https://apnews.com/article/nato-ukraine-summit-zelenskyy-trump-2e95a3f3426d9037b7d1a89765f55a82"

"June 23","NATO chief says Ukraine remains vital at summit despite Zelenskyy’s absence","NATO chief Rutte said Ukraine is a vital topic despite Zelenskyy's absence at the meeting.","https://apnews.com/article/nato-ukraine-rutte-zelenskyy-trump-war-fa7230a5162dca8a814d8e4d68ed87b7"

"June 24","Russian attacks kill 26 civilians in Ukraine as Zelenskyy seeks more Western help","Russian missile/drone/artillery attacks killed at least 26 civilians in Ukraine.","https://apnews.com/article/russia-ukraine-war-drone-missile-attacks-8135ed1141c667b5b044b8187b2d2179"

"April 24","Zelenskyy says he’s cutting short a visit to South Africa after Russian attacks on Kyiv","Zelenskyy cut short his South Africa visit due to a major Russian attack on Kyiv.","https://apnews.com/article/zelenskyy-ukraine-russia-war-trump-south-africa-aac31e008039b3afbd45ed9fe482e3fa"

"August 30","Russian drone and missile attack on southern Ukraine kills 1 and wounds dozens","A major aerial attack on southern Ukraine killed one and injured dozens.","https://apnews.com/article/russia-ukraine-war-drone-missile-strike-attack-airstrike-a1769401dde9ede9e11810029ccd0abf"

"July 31","Ukraine’s Parliament approves law restoring independence of anti-graft watchdogs","Ukraine's parliament restored the independence of key anti-corruption watchdogs.","https://apnews.com/article/russian-ukraine-war-corruption-law-graft-watchdogs-2abf1e53a71ed0fff726c256c55aefb8"

"July 25","Ukraine’s Zelenskyy says defenses are holding firm against Russia’s summer push","Zelenskyy said Ukraine’s forces are holding back Russia’s summer offensive.","https://apnews.com/article/russia-ukraine-war-zelenskyy-front-line-e69e6b1a6ce4b6cc02b6899d945ddeab"

"August 3","Ukrainian drone attack sets Russian oil depot on fire as Zelenskyy announces prisoner exchange","A Ukrainian drone attack ignited a major fire at a Russian oil depot.","https://apnews.com/article/russia-ukraine-war-depot-drones-missiles-ceasefire-1bf8440535e8fa32bc66310ea37658d4"

"August 11","Trump suggests he’ll know quickly if Putin wants peace in upcoming talks","Trump said he will quickly know if Putin wants to make a peace deal with Ukraine.","https://apnews.com/article/russia-ukraine-war-drone-strike-575aa4ce590256d50a9d73911f681269"

"August 14","Zelenskyy meets Starmer in London ahead of Trump-Putin summit","Zelenskyy met UK PM Starmer a day before the Trump–Putin summit.","https://apnews.com/video/zelenskyy-meets-starmer-in-london-ahead-of-trump-putin-summit-4e7e358e674b488da39e8be46a8478cd"

"November 6","Ukraine says it has hit a major Russian oil refinery with long-range drones","Ukraine struck a major oil refinery in Russia’s Volgograd region.","https://apnews.com/article/russia-ukraine-war-oil-refinery-energy-infrastructure-5bcdc5753cb9fa64f45c276223c1d8c8"

"June 16","Ukraine’s Zelenskyy wins non-military backing from Austria","Zelenskyy won non-military support from Austria one day before a G7 visit.","https://apnews.com/article/zelenskyy-bellen-stocker-austria-ukraine-russia-nehammer-b34378ff9e1dee50d84c952955e609a7"

"August 28","Zelenskyy says Russia’s bombardment of Kyiv shows Putin wants to continue war","Zelenskyy said Russia's massive bombardment shows Putin wants to continue the war.","https://apnews.com/video/zelenskyy-says-russias-bombardment-of-kyiv-shows-putin-wants-to-continue-war-8b6f423dcb364333bee4789c8a87b8fc"

"September 5","Zelenskyy tells forum Ukraine is preparing strength to pressure Russia towards peace","Zelenskyy said Ukraine is building a new multi-domain security system to pressure Russia toward peace.","https://apnews.com/video/zelenskyy-tells-forum-ukraine-is-preparing-strength-to-pressure-russia-towards-peace-091e1c4c20fa425cb5f094a661bfddf8"

"May 14","Brazil’s Lula says he would try to urge Putin to negotiate with Zelenskyy","Brazil’s Lula said he would try to get Putin to attend talks with Zelenskyy.","https://apnews.com/article/russia-ukraine-talks-putin-brazil-lula-dee5556c69741e32492ed850f77c1517"

"Yesterday","Ukrainian President visits anti-war painting Guernica in Madrid with Spanish PM Sánchez","Zelenskyy visited Picasso’s anti-war painting “Guernica” in Madrid.","https://apnews.com/video/ukrainian-president-visits-anti-war-painting-guernica-in-madrid-with-spanish-pm-sanchez-75e63368da414366ac6e5ca4500c9a68"

"October 12","Trump warns Russia he may send long-range Tomahawks if Moscow doesn’t settle war soon","Trump warned Russia he may send Ukraine Tomahawk missiles if the war continues.","https://apnews.com/article/trump-tomahawk-missiles-russia-ukraine-war-522fb8bb8fe8ce87107e1eb320abae0e"

"September 15","Trump says ‘hatred between Zelenskyy and Putin is unfathomable’","Trump said the hatred between Zelenskyy and Putin is so deep they “almost can’t talk.”","https://apnews.com/video/trump-says-hatred-between-zelenskyy-and-putin-is-unfathomable-915d1c4289c840fbb8c73a34059d1b67"

"August 24","‘We are strong and not alone,’ says Zelenskyy as Ukraine marks independence day","Zelenskyy said Ukraine is strong and supported as it marked independence day.","https://apnews.com/video/we-are-strong-and-not-alone-says-zelenskyy-as-ukraine-marks-independence-day-3d2c33f3774443e5bfd4fdcca9c9df39"

"August 29","Zelenskyy visits latest missile attack site in Kyiv","Zelenskyy visited the site of a missile attack that killed several civilians.","https://apnews.com/video/zelenskyy-visits-site-of-the-latest-missile-attack-in-ukrainian-capital-kyiv-4f8ebdc60a424512be02da24a410bf93"

"August 17","Zelenskyy visits EU headquarters ahead of Washington summit","Zelenskyy met with EU Commission President von der Leyen ahead of a summit.","https://apnews.com/video/zelenskyy-visits-eu-headquarters-ahead-of-washington-summit-4be76aa2b26b441e8803be5417495c46"

"August 18","‘I changed, you did not’: Zelenskyy replies to reporter who asked about his suit","Zelenskyy joked with a reporter about changing from his usual attire.","https://apnews.com/video/zelenskyys-attire-comes-up-second-time-in-oval-office-d0a28f901ac849da847f56ecae6ea608"

"May 12","Zelenskyy hopes for ceasefire with Russia and challenges Putin to meet him in Turkey","Zelenskyy challenged Putin to personally attend ceasefire talks in Turkey.","https://apnews.com/article/russia-ukraine-war-ceasefire-2b3d2fad88436c5406ea63f81ac554ef"
"August 14","Zelenskyy arrives meets with UK PM Keir Starmer in London; pair ignore reporters’ questions","UK Prime Minister Keir Starmer welcomed Ukrainian President Volodymyr Zelenskyy in London ahead of a major U.S.–Russia summit.","https://apnews.com/video/zelenskyy-arrives-meets-with-uk-pm-keir-starmer-in-london-pair-ignore-reporters-questions-6a4d46da46e945a680f206581d28c71b"

"August 18","Zelenskyy signals openness to three-way meeting with Trump and Putin","Zelenskyy said Trump will try to organize a trilateral meeting between Ukraine, Russia and the United States.","https://apnews.com/video/zelenskyy-signals-openness-to-three-way-meeting-with-trump-and-putin-5178939250ee4e74a2a9d61d3d25600b"

"August 12","Land swaps with Russia are not only unpopular in Ukraine. They’re also illegal","Zelenskyy says any peace deal requiring Ukraine to give up territory would violate the Ukrainian constitution.","https://apnews.com/article/russia-ukraine-land-swap-trump-summit-e8e869d5d5ec672fee3e86022b20d11a"

"April 20","Zelenskyy says Russia is trying to create an ‘impression of a ceasefire’ as attacks continue","Zelenskyy accused Russia of attacking immediately after declaring an Easter ‘truce.’","https://apnews.com/article/russia-ukraine-easter-ceasefire-zelenskyy-putin-attacks-934e5c2a493be32b605ddb84d955b34b"

"August 7","Zelenskyy says Ukraine should take part in US negotiations with Russia","Zelenskyy says Ukraine must be included in any US–Russia peace discussions.","https://apnews.com/video/zelenskyy-says-ukraine-should-take-part-in-us-negotations-with-russia-173f5469db264786957c53641ba40d18"

"October 12","Russia attacks Ukraine’s power grid as Moscow worries over US Tomahawk missiles","Russia targeted Ukraine’s power grid in an escalating campaign against energy infrastructure.","https://apnews.com/article/russia-ukraine-energy-drones-zelenskyy-sanctions-tomahawks-95e542fb1030e7e89fc8ac45afe3307a"

"October 6","Ukraine says it struck Russian ammunition plant, oil terminal and weapons depot","Ukraine launched long-range drone and missile strikes against key Russian sites including an ammunition plant.","https://apnews.com/article/russia-ukraine-war-drones-oil-terminal-ef62f837224a387e7eed9be6b256e42c"

"August 28","Germany’s Merz says he believes it is ‘clear’ Putin-Zelenskyy meeting will not happen","Germany’s Chancellor Merz said a direct Putin-Zelenskyy meeting is unlikely.","https://apnews.com/video/germanys-merz-says-he-believes-it-is-clear-putin-zelenskyy-meeting-will-not-happen-240405673cd64b12b714cc72e446d91b"

"August 19","Despite a flurry of meetings on Russia’s war in Ukraine, major obstacles to peace remain","Trump and Zelenskyy held their second Oval Office meeting, which went smoothly compared to February.","https://apnews.com/article/russia-ukraine-war-trump-europe-next-steps-527983fab40e58208e9e18c943de696a"

"March 1","Zelenskyy embraced by British prime minister a day after White House blowout","The UK reaffirmed support for Ukraine one day after Zelenskyy’s contentious meeting with Trump.","https://apnews.com/article/zelenskyy-starmer-uk-british-white-house-trump-a05e6ec1c37aabdbb5067d8ce87d6d1e"

"October 10","Russian strikes wound at least 20 in Kyiv as child is killed in separate attack","Russian drone/missile attacks injured 20 and caused major damage in Kyiv.","https://apnews.com/article/ukraine-russia-war-airstrikes-74c456c48b64e93300b4cf05bc60f6dd"

"October 22","Trump levies new sanctions on Russian oil giants in a push on Putin to end Ukraine war","Trump imposed sweeping sanctions on Russia’s oil sector to pressure Putin.","https://apnews.com/article/russia-ukraine-drones-war-putin-trump-2cf465171be371a29e24aa600293b691"

"August 13","Zelenskyy arrives in Berlin to speak to allies ahead of Trump-Putin summit","Zelenskyy and German leaders prepared coordinated positions ahead of a Trump-Putin summit.","https://apnews.com/video/zelenskyy-arrives-in-berlin-to-speak-to-allies-ahead-of-trump-putin-summit-3f59e0e4a87f4a82a40ab0f477a1b153"

"April 24","Trump says Zelenskyy is prolonging war by resisting calls to cede Crimea to Russia","Trump criticized Zelenskyy for refusing to hand Crimea to Russia in peace proposals.","https://apnews.com/article/russia-ukraine-war-peace-talks-london-4f35dc70f521e2363218f4c40748caba"

"June 23","Russian attacks on Ukraine kill 14 civilians as Zelenskyy travels to UK","Russian drone/missile attacks killed 14 including 9 in Kyiv.","https://apnews.com/article/russian-ukraine-war-attack-kyiv-deaths-injuries-aed85e211f1e43928b5bf52d718c1892"

"May 15","Putin spurns Zelenskyy meeting but lower-level Ukraine-Russia talks are still on","Putin rejected Zelenskyy’s proposal for a direct meeting but lower-level talks will proceed.","https://apnews.com/article/russia-ukraine-war-istanbul-talks-zelenskyy-putin-05795eea960b9035f93a143c3e177c3d"

"August 19","Zelenskyy thanks Trump multiple times during meeting","Zelenskyy publicly expressed gratitude to Trump after past tensions.","https://apnews.com/video/zelenskyy-thanks-trump-multiple-times-during-meeting-d559b5dd75bc428da5e6f2379472c83e"

"August 18","Zelenskyy signals openness to three-way meeting with Trump and Putin","Zelenskyy said a trilateral negotiation may be possible.","https://apnews.com/video/zelenskyy-signals-openness-to-three-way-meeting-with-trump-and-putin-4b25249826104d09a35ead9c29896878"

"April 22","Zelenskyy pushes back on ceding Ukrainian land in potential peace deal ahead of London talks","Zelenskyy rejected surrendering Ukrainian territory as part of peace conditions.","https://apnews.com/article/russia-ukraine-war-drone-attack-peace-talks-be98e85000b8e0f24a2d7ada71f3861d"

"August 2","Zelenskyy visits site of deadly Russian attack on Kyiv which killed 31 people","Zelenskyy visited the aftermath of a major missile/drone attack in Kyiv.","https://apnews.com/video/zelenskyy-visits-site-of-deadly-russian-attack-on-kyiv-which-killed-31-people-beddd6096a5f4cf4a468969d38eb6393"

"October 30","Russia blasts Ukraine’s power grid again, causing outages and killing 6","Russia launched another massive strike on Ukraine’s energy grid.","https://apnews.com/article/russia-ukraine-war-attack-power-outages-2110169707d2d8c7757ce4fc807cff4c"

"October 11","Power restored to 800,000 in Kyiv after major Russian strikes","More than 800,000 regained electricity after large-scale Russian attacks.","https://apnews.com/article/russia-ukraine-war-power-grid-assets-fe589dd9e12368d071fdfedf8819c15e"

"October 26","Russia targets Kyiv with drones, killing 3 and wounding 29","A drone strike killed three people in Kyiv homes.","https://apnews.com/article/russia-ukraine-war-kyiv-722cd709e7e25266c4a67df6913cdc72"

"August 9","Zelenskyy rejects formally ceding territory, says Kyiv must be part of negotiations","Zelenskyy insisted Kyiv must participate in any negotiations.","https://apnews.com/video/zelenskyy-rejects-formally-ceding-ukrainian-territory-says-kyiv-must-be-part-of-any-negotiations-5ded6552583145aea95756c582b83edf"

"August 18","Ukraine’s Zelenskyy arrives at White House to meet Trump on ending Russia’s war","Zelenskyy arrived with a large European delegation for peace talks.","https://apnews.com/video/ukraines-zelenskyy-arrives-at-white-house-to-meet-trump-on-ending-russias-war-ae5ebc91ab964e6fb9921a90acbee41a"

"October 13","Ukraine’s daily moment of remembrance endures through intensified Russian attacks","Every morning, Ukraine pauses for a nationwide minute of silence.","https://apnews.com/article/ukraine-russia-war-kyiv-remembrance-ea1591300a9e0baaa4b0071b271bcb54"

"August 18","Trump and Zelenskyy strike a different mood from their last Oval Office meeting","The tone of the Oval Office meeting was noticeably calmer than in February.","https://apnews.com/video/trump-and-zelenskyy-strike-a-different-mood-from-their-last-oval-office-meeting-61a94b2853ad4f48aef7cb0f0a86cc3d"

"August 18","European leaders arrive at the White House for talks with Trump and Zelenskyy","European leaders joined Zelenskyy and Trump for peace meetings.","https://apnews.com/video/european-leaders-arrive-at-the-white-house-for-talks-with-trump-and-zelenskyy-on-the-ukraine-war-5a384a7734134f1db2464a62817ca7aa"

"October 23","US and allies increase sanctions on Russia to push Putin into peace talks","The EU and US issued new sanctions targeting Russia’s oil sector.","https://apnews.com/article/russia-ukraine-war-europe-us-sanctions-f9d98cd011533b6f1c071ea2cef9f2d9"

"March 30","Trump finds fault with both Putin and Zelenskyy as he tries to push for deal","Trump criticized both leaders as he attempted to push a peace agreement.","https://apnews.com/article/russia-ukraine-war-drones-kharkiv-offensive-1d2f793cc99798b0e491b9dde8e0cee0"
"August 18","European leaders join Trump and Zelenskyy for critical talks on ending Russia’s war in Ukraine","European leaders joined Zelenskyy and Trump at the White House for critical discussions aimed at ending Russia’s war.","https://apnews.com/video/european-leaders-join-trump-and-zelensky-for-critical-talks-on-ending-russias-war-in-ukraine-9f943d0404dc49fbacf884cfbd1d0afe"

"July 21","New round of Russia-Ukraine peace talks set for Wednesday, Zelenskyy says","Zelenskyy said Ukraine and Russia would hold another round of peace talks on Wednesday.","https://apnews.com/video/new-round-of-russia-ukraine-peace-talks-set-for-wednesday-zelenskyy-says-63f46abef1ef450f80bc93a6c2867710"

"August 12","Zelenskyy tells youth forum Putin and Trump cannot agree on anything without Ukraine present","Zelenskyy told a youth forum that Trump and Putin cannot decide anything about Ukraine without Ukraine being present.","https://apnews.com/video/zelenskyy-tells-youth-forum-putin-and-trump-cannot-agree-on-anything-without-ukraine-present-7a81afb29f6541fbaff715c30556b184"

"September 23","Trump says he now believes Ukraine can win back all territory lost to Russia with NATO’s help","Trump said he now believes Ukraine can win back all territory taken by Russia with NATO’s support.","https://apnews.com/article/russia-ukraine-war-un-zelenskyy-trump-f28942b3915e40226654548bb3ee7919"

"August 15","Demonstrators in Alaska skeptical of Trump-Putin meeting without Zelenskyy","Protesters in Alaska objected to a Trump–Putin meeting that excluded Zelenskyy.","https://apnews.com/video/demonstrators-in-alaska-skeptical-of-trump-putin-meeting-without-zelenskyy-37d63f64e5d44800afa2ef375c0f3bfc"

"August 21","Lavrov: Putin willing to meet for talks with Zelenskyy pending ‘issues’ being ‘well worked out’","Lavrov said Putin is willing to meet Zelenskyy if certain issues are resolved.","https://apnews.com/video/lavrov-putin-willing-to-meet-for-talks-with-zelenskyy-pending-issues-being-well-worked-out-dc0e96e80e584325a177c176d0dd4fd7"

"August 22","Trump frustrated after thinking he made headway on Russia-Ukraine talks only to see Putin balk","Trump believed progress was made toward Russia–Ukraine talks, only for Putin to balk.","https://apnews.com/article/russia-ukraine-war-trump-putin-demands-2bada6d1084555d965f06e16d2d97b2a"

"August 13","In his own words: Trump’s evolving rhetoric about Zelenskyy and Putin","Trump’s remarks about Zelenskyy and Putin have shifted significantly ahead of a planned Alaska summit.","https://apnews.com/video/in-his-own-words-trumps-evolving-rhetoric-about-zelenskyy-and-putin-5cfd2abb2aaa43fea710fc60bb526ccd"

"August 18","Italian PM meets Zelenskyy and other European leaders ahead of Trump summit","Italy’s Prime Minister met Zelenskyy and European leaders in Washington before a Trump–Putin summit.","https://apnews.com/video/italian-pm-meets-zelenskyy-and-other-european-leaders-ahead-of-trump-summit-4d6cc17d6feb4a709b89ee1d9eaab98c"

"July 20","Zelenskyy says Ukraine proposed to Russia to hold next round of talks next week","Zelenskyy said Ukraine proposed to Russia to resume peace talks next week.","https://apnews.com/video/zelenskyy-says-ukraine-proposed-to-russia-to-hold-next-round-of-talks-next-week-720441f714ea4daba976890c252e05bb"

"October 23","EU leaders agree to future Ukraine funds but make little headway on a plan to use Russia’s assets","EU leaders ordered new proposals on funding Ukraine and discussed using frozen Russian assets.","https://apnews.com/article/europe-russia-ukraine-assets-frozen-war-belgium-ea3ae2435aa9967e2728e73b4708dd9b"

"March 3","Russia relishes Trump-Zelenskyy spat and accuses Ukraine and European allies of warmongering","Russia welcomed tensions between Trump and Zelenskyy, hoping it would weaken U.S. support for Ukraine.","https://apnews.com/article/russia-us-trump-zelenskyy-putin-ukraine-war-d718060c5eb315e84f054bb8bf703b10"

"July 14","Zelenskyy meets with US envoy Kellogg as US pledges more Patriot missiles to Ukraine","Zelenskyy met U.S. envoy Kellogg as Washington prepared to send more Patriot systems.","https://apnews.com/video/zelenskyy-meets-with-us-envoy-kellogg-as-us-pledges-more-patriot-missiles-to-ukraine-b5956bbcb8a5418eb8d944c90edb1b6a"

"September 11","Zelenskyy meets US envoy Kellogg in Kyiv, on day after Russian drone incursion in Poland","Zelenskyy met the U.S. envoy after a Russian drone entered Polish airspace.","https://apnews.com/video/zelenskyy-meets-us-envoy-kellogg-in-kyiv-on-day-after-russian-drone-incursion-in-poland-1e1eddddc9d142aeb1f2f07d4bfc0f7a"

"August 3","Ukrainian anti-corruption agencies uncover drone procurement graft scheme","Ukraine uncovered a drone procurement bribery scheme after restoring watchdog independence.","https://apnews.com/article/russian-ukraine-war-corruption-law-graft-drone-02aaa100244f82f41fea68c6b727e6a8"

"October 5","At least 5 people are killed in a large-scale Russian attack on Ukraine","Russia launched a large-scale drone and missile strike across Ukraine, killing at least five.","https://apnews.com/article/russia-ukraine-war-invasion-drones-drone-strike-attack-b6e20002e1b62e3c5a3b8590f7a2d556"

"August 11","Europe and Ukraine leaders seek talks with Trump to defend their interests ahead of US-Russia summit","Ukraine and European leaders sought talks with Trump to safeguard their interests before a U.S.–Russia summit.","https://apnews.com/article/europe-ukraine-territory-russia-trump-putin-summit-5d2079bd13561edac7752d338ea7b93c"

"August 18","Zelenskyy, Trump express hope for trilateral talks with Putin to bring end to Russia-Ukraine war","Trump and Zelenskyy expressed hope for trilateral talks with Putin to end the war.","https://apnews.com/video/zelenskyy-trump-express-hope-for-trilateral-talks-with-putin-to-bring-end-to-russia-ukraine-war-a2a779cb51dc4305a93ce18189b51c61"

"August 18","Zelenskyy, Trump express hope for trilateral talks with Putin to bring end to Russia-Ukraine war","Trump and Zelenskyy repeated hope for three-way talks aimed at ending the conflict.","https://apnews.com/video/zelenskyy-trump-express-hope-for-trilateral-talks-with-putin-to-bring-end-to-russia-ukraine-war-a13d5e8e60024c0e88a7817a2528a0da"

"February 28","What they said: Trump, Zelenskyy and Vance’s heated argument in the Oval Office","Trump and Vance accused Zelenskyy of lacking gratitude during a heated Oval Office exchange.","https://apnews.com/article/trump-zelenskyy-vance-transcript-oval-office-80685f5727628c64065da81525f8f0cf"

"September 20","Russia launches a large-scale attack on Ukraine, killing 3 and wounding dozens","Russia launched missiles, drones and glide bombs across Ukraine, killing three.","https://apnews.com/article/russia-ukraine-missile-drone-attack-zelenskyy-b517772651a4c95c8d66ce2777c544ff"

"February 14","Zelenskyy to Vance: Ukraine wants ‘security guarantees’ as Trump seeks to end Ukraine-Russia war","Zelenskyy said Ukraine needs firm security guarantees before peace talks.","https://apnews.com/article/vance-rubio-munich-security-conference-ukraine-ab2d7379aaf6ca224cc51e1f9ade9edf"

"April 9","Ukraine’s Zelenskyy says 2 Chinese men were caught fighting alongside Russia","Zelenskyy said Ukraine captured two Chinese men fighting for Russia.","https://apnews.com/article/russia-ukraine-war-captured-chinese-141294997b4c63c67f978121db645244"

"July 24","Zelenskyy moves to restore anti-corruption agencies’ independence after public outcry","Zelenskyy submitted a bill restoring watchdog independence after mass protests.","https://apnews.com/video/zelenskyy-moves-to-restore-anti-corruption-agencies-independence-after-public-outcry-935b1f1159544b7586a7cc397c80cdd4"

"August 18","Zelenskyy brings Europe’s top leaders with him to meet Trump on ending Russia’s war","Zelenskyy brought top EU leaders to Washington for peace talks with Trump.","https://apnews.com/video/zelenskyy-brings-europes-top-leaders-with-him-to-meet-trump-on-ending-russias-war-422fda1e0d4249c0aa882f1573c8466d"

"August 22","Trump says he would ‘rather not’ be part of a Putin Zelenskyy meeting","Trump said he would prefer not to join a potential Putin–Zelenskyy meeting.","https://apnews.com/video/trump-says-he-would-rather-not-be-part-of-a-putin-zelenskyy-meeting-c2a5fddf28e64a96855a09f39b1bd81c"

"March 1","Ukrainians rally around Zelenskyy as defender of national interest after Oval Office blowout","Ukrainians rallied around Zelenskyy following a contentious Oval Office meeting with Trump.","https://apnews.com/article/oval-office-blowout-ukrainians-rally-zelenskyy-af89022fa54f57113666f180e23e2edd"

"September 24","Ukraine’s president says the world is in ‘the most destructive arms race in history’","Zelenskyy said the world is entering the most destructive arms race in history.","https://apnews.com/video/ukraines-president-says-the-world-is-in-the-most-destructive-arms-race-in-history-31835fbd0d5e4421b777e39522f1b7eb"

"February 19","Trump and Zelenskyy trade barbs as US-Ukraine relations sour over the war with Russia","Relations between Trump and Zelenskyy worsened amid disagreements over the war.","https://apnews.com/article/russia-ukraine-war-kellogg-zelenskyy-437f4c8fa4531059007dd3ab00c23458"

"September 24","Some leaders at UN condemn ‘sick expression of joy,’ ‘macabre response’ to Charlie Kirk’s killing","World leaders at the UN condemned reactions to the killing of activist Charlie Kirk.","https://apnews.com/article/charlie-kirk-un-general-assembly-serbia-515ed8e65e2b8424da6dce20c9b6eb2a"
"February 20","US official says Trump’s frustration with Zelenskyy is ‘multifold’ and blasts ‘insults’ from Ukraine","A top White House official said Trump’s increasing criticism reflects frustration with Zelenskyy’s perceived roadblocks to ending the war.","https://apnews.com/article/trump-zelenskyy-frustrations-1cc3076d20c0933b513ced96bd6ddd26"

"March 3","Following Trump’s lead, his allies criticize Ukraine’s Zelenskyy and suggest he may need to resign","Trump’s allies echoed his criticism and suggested Zelenskyy may need to resign amid tensions over war strategy.","https://apnews.com/article/trump-zelenskyy-resign-ukraine-russia-war-f258a45da0b3d990d3b2f566c2ff8139"

"September 29","Russian drone and missile attack on Ukraine kills at least 4 people and wounds 70","Russia launched a major drone and missile attack on Kyiv, killing at least four people and injuring 70.","https://apnews.com/article/ukraine-russia-kyiv-drone-attack-df3ec471bacd7395d408cc0d7e68f8b4"

"March 5","Kremlin says a 2022 Ukrainian decree bans Zelenskyy from talks with Putin","Russia questioned how Ukraine can join peace talks when a 2022 decree bans negotiations with Putin.","https://apnews.com/article/russia-ukraine-war-putin-zelenskyy-peace-kremlin-4b562918462856b9020147fc50b37b16"

"March 4","Zelenskyy calls Oval Office spat with Trump ‘regrettable,’ says he’s ready to work for Ukraine peace","Zelenskyy said last week’s Oval Office blowup with Trump was regrettable and urged a reset.","https://apnews.com/article/russia-ukraine-war-trump-zelenskyy-military-aid-2ce8b167f0ba948b2b606381192de71d"

"July 11","Zelenskyy says aid shipments from the U.S. ‘have been restored’","Zelenskyy said paused U.S. military aid shipments have resumed.","https://apnews.com/video/zelenskyy-says-aid-shipments-from-the-u-s-have-been-restored-aae1802a3d664086b73a6fdc71a3c55e"

"October 1","Denmark warns that Russia is waging a hybrid war on Europe, as EU leaders hold security talks","Denmark warned Europe is in a hybrid war with Russia and must arm itself.","https://apnews.com/article/europe-drones-russia-defense-security-ukraine-ef7b332d66117beb702aa620b649ebf9"

"August 18","Zelenskyy and Europe’s top leaders will meet with Trump on ending Russia’s war, AP Explains","Zelenskyy and top EU leaders will meet Trump in Washington to discuss ending the war.","https://apnews.com/video/zelenskyy-and-europes-top-leaders-will-meet-with-trump-on-ending-russias-war-ap-explains-9ff9abf42363413aad46790980d8c4fc"

"April 26","Zelenskyy and Trump talk as they attend the funeral of Pope Francis in Vatican","Zelenskyy and Trump met briefly while attending Pope Francis' funeral in the Vatican.","https://apnews.com/video/zelenskyy-and-trump-talk-as-they-attend-the-funeral-of-pope-francis-in-vatican-f544acf7c9dd4daa934614a3d2af40a9"

"August 21","Trump thanks Ukrainian serviceman for veteran’s golf putter presented to him by Zelenskyy","Zelenskyy gave Trump a golf putter that belonged to a Ukrainian serviceman.","https://apnews.com/video/trump-thanks-ukrainian-serviceman-for-veterans-golf-putter-presented-to-him-by-zelenskyy-cb67215c05904e2ba4dd8a3e22656d8e"

"August 6","Trump says ‘there’s a good chance there will be a meeting very soon’ with Putin and Zelenskyy","Trump said a meeting with Putin and Zelenskyy may happen soon.","https://apnews.com/video/trump-says-theres-a-good-chance-there-will-be-a-meeting-very-soon-with-putin-and-zelenskyy-6c713fa042e6463eb1358b075552de48"

"September 4","Macron says 26 countries pledge troops as a reassurance force for Ukraine after war ends","Macron said 26 allies pledged troops for a postwar reassurance force.","https://apnews.com/article/russia-ukraine-war-witkoff-europe-61ae60275a00cb442c743181df13b785"

"October 1","Ukrainian nuclear plant’s longest power outage since war began is ‘critical’ moment","Zaporizhzhia nuclear plant suffered its longest outage since the war began.","https://apnews.com/article/ukraine-russia-war-nuclear-zaporizhzhia-a0273ea4558a7b26cf232edd620942cc"

"March 1","The Latest: Most European leaders back Zelenskyy as he joins crisis talks in London","Zelenskyy joined crisis talks in London and thanked U.S. leadership despite prior tensions.","https://apnews.com/article/russia-ukraine-war-zelenskyy-london-bf158d8f9e10a7c049ea90f8fd917ab6"

"March 3","Ukraine’s Zelenskyy says end of war with Russia is ‘very, very far away’","Zelenskyy said a deal to end the war remains very far away.","https://apnews.com/article/russia-ukraine-war-zelenskyy-starmer-trump-b025877c40ffe0ddf2a92adad1715231"

"March 2","What US lawmakers are saying about the White House clash between Trump and Zelenskyy","Republicans and Democrats reacted to the Oval Office confrontation.","https://apnews.com/article/republicans-trump-zelenskyy-meeting-64ec4a67fce4f04a2d189a1e0204b023"

"February 21","US envoy praises Zelenskyy after Trump’s censure of the Ukrainian leader","The U.S. envoy said discussions with Zelenskyy were positive despite Trump's criticism.","https://apnews.com/article/russia-ukraine-zelenskyy-trump-0bc41d62c4fdfa00b4358f9043ee9991"

"September 4","Trump covers Zelenskyy call, RFK Jr., NYC mayor race and jobs report at a White House dinner","Trump answered questions about his Zelenskyy call and political issues at a private dinner.","https://apnews.com/video/trump-covers-zelenskyy-call-rfk-jr-nyc-mayor-race-and-jobs-report-at-a-white-house-dinner-2618cf83e33b4ce087f681c0c69207cb"

"June 2","After talks with Zelenskyy and Macron, US senators warn: Putin ‘is preparing for more war’","US senators warned Russia is preparing a new offensive.","https://apnews.com/article/ukraine-russia-sanctions-graham-blumenthal-b2b9b69f504b8afd064055bb3bf11800"

"July 15","Ukraine’s prime minister resigns, opening the door to a broad government reshuffle","Ukraine's PM resigned ahead of a likely major government reshuffle.","https://apnews.com/article/russia-ukraine-war-government-reshuffle-966f2a08d1ad88d9a0947e62b9e14ee9"

"February 8","Zelenskyy confirms a new Ukrainian offensive in Russia’s Kursk region","Zelenskyy confirmed Ukrainian forces launched an offensive in Russia's Kursk region.","https://apnews.com/article/russia-ukraine-north-korea-kursk-de43ba469a070a4700ba26f330131b49"

"March 4","Trump and Zelenskyy through the years: From a ‘perfect’ call to pausing US assistance to Ukraine","A look at the history between Trump and Zelenskyy from 2019 to present.","https://apnews.com/article/trump-zelenskyy-past-relationship-shouting-oval-office-88690f790901687fc1587f1bf89f5036"

"July 26","Zelenskyy calls for ramped up production of drone interceptors after Russian glide bomb attack","Zelenskyy urged rapid expansion of drone interceptor production.","https://apnews.com/video/zelenskyy-calls-for-ramped-up-production-of-drone-interceptors-after-russian-glide-bomb-attack-af4e8d298d2d4dfd82175854298ca2cf"

"July 9","Pope Leo hosts Ukraine’s Zelenskyy at summer residence in Castel Gandolfo","Zelenskyy met Pope Leo XIV to discuss kidnapped Ukrainian children and possible peace talks.","https://apnews.com/video/pope-leo-hosts-ukraines-zelenskyy-at-summer-residence-in-castel-gandolfo-c5f233f89f964ca288372e524d674bd2"

"July 9","Ukrainian President Zelenskyy meets Trump’s special envoy for Ukraine Keith Kellogg in Rome","Zelenskyy met with Trump’s special envoy Keith Kellogg in Rome.","https://apnews.com/video/ukrainian-president-zelenskyy-meets-trumps-special-envoy-for-ukraine-keith-kellogg-in-rome-5114010d060e483c9452e269e2aed1e1"

"February 28","Zelenskyy leaves White House without signing minerals deal after Oval Office blowup","Trump berated Zelenskyy, then canceled the minerals deal signing.","https://apnews.com/article/zelenskyy-security-guarantees-trump-meeting-washington-eebdf97b663c2cdc9e51fa346b09591d"

"March 4","Without US help, Zelenskyy has few options except to repair his relationship with the White House","Zelenskyy faces limited options after a major Oval Office confrontation.","https://apnews.com/article/russia-ukraine-war-trump-zelenskyy-meeting-30be085063f4f6f3df242553402234f1"

"April 5","Zelenskyy meets European military leaders to plan for a peacekeeping force","Zelenskyy met European military leaders to discuss a multinational peacekeeping force.","https://apnews.com/article/russia-ukraine-war-kryvyi-rih-dnipropetrovsk-fcdb5bbec7a51365b08e8ef2884ba22f"

"February 17","Zelenskyy travels to UAE as momentum grows for talks to end Russia’s war in Ukraine","Zelenskyy traveled to the UAE amid growing momentum for peace talks.","https://apnews.com/article/uae-russia-ukraine-war-a09b2fc2d81276551f40d89383a348c2"

"February 23","Zelenskyy says progress made on reaching an agreement with the US on rare minerals deal","Zelenskyy said the U.S. dropped a controversial minerals profits proposal.","https://apnews.com/article/russia-ukraine-war-drones-anniversary-putin-trump-c8f73a98d071055be52a1b22b0785ecc"
"May 17","Canadian PM Mark Carney meets with Ukraine President Zelenskyy in Rome","Canadian Prime Minister Mark Carney met with Ukrainian President Volodymyr Zelenskyy at the country’s Official Residence to the Italian Republic in Rome on Saturday.","https://apnews.com/video/canadian-pm-mark-carney-meets-with-ukraine-president-zelenskyy-in-rome-9baf3580e42042d19e5a6f074366f68e"

"May 28","German Chancellor Merz welcomes Ukraine’s Zelenskyy to Berlin","Ukrainian President Volodymyr Zelenskyy met with new German Chancellor Friedrich Merz in Berlin as Kyiv seeks further military support.","https://apnews.com/video/german-chancellor-merz-welcomes-ukraines-zelenskyy-to-berlin-7d65cf0903684772b250acd55da4d64d"

"August 12","The diplomatic efforts that led to the Trump-Putin meeting on Ukraine","Russian President Vladimir Putin is set to meet U.S. President Donald Trump in Alaska as part of efforts to end Ukraine’s war.","https://apnews.com/article/russia-ukraine-war-diplomatic-putin-trump-2a2c4bda9bb53ae2036837af899573a3"

"June 2","Zelenskyy says he backs Turkish proposal for a meeting with Trump and Putin","Zelenskyy said he supports Turkey’s proposal to organize a meeting between him, Trump and Putin.","https://apnews.com/video/zelenskyy-says-he-backs-turkish-proposal-for-a-meeting-with-trump-and-putin-79efa1baa2174e3ca91a5ddf328b35c2"

"April 15","NATO chief visits wounded soldiers in Odesa with Zelenskyy","Zelenskyy and NATO chief Mark Rutte visited wounded soldiers in an Odesa hospital.","https://apnews.com/video/nato-chief-visits-wounded-soldiers-in-odesa-with-zelenskyy-1a04e40d3b9a45719d80ca176aea92c2"

"February 13","Russia rejoices at Trump-Putin call as Zelenskyy rejects talks without Ukraine present","Russian officials celebrated Trump’s plan to meet Putin, while Zelenskyy insisted Ukraine must be present.","https://apnews.com/article/russia-ukraine-war-trump-putin-9bd931d9ffde1bb573fae514efb29ddd"

"June 26","Zelenskyy calls for strong sanctions and oil price cap in address to European Council","Zelenskyy urged EU leaders to impose strong sanctions and a strict oil price cap.","https://apnews.com/video/zelenskyy-calls-for-strong-sanctions-and-oil-price-cap-in-address-to-european-council-cdc854fd1d72461a81016c1634efefb0"

"August 19","FACT FOCUS: Trump says he has ended seven wars. The reality isn’t so clear cut","Trump claims to have ended several wars, though evidence is mixed.","https://apnews.com/article/trump-peace-wars-claim-fact-check-10128b26232e1d1eb9e68c5617320cf3"

"May 14","Zelenskyy ‘waiting to see who will come from Russia’ for talks in Turkey","Zelenskyy said he is waiting to see who Russia will send to ceasefire talks in Turkey.","https://apnews.com/video/zelenskyy-waiting-to-see-who-will-come-from-russia-for-talks-in-turkey-ec900da6b4fc4799a8dbca9356682d62"

"June 24","Ukraine’s Zelenskyy meets UK PM Starmer and British troops in London","Zelenskyy and UK PM Keir Starmer met troops training Ukrainian soldiers.","https://apnews.com/video/ukraines-zelenskyy-meets-uk-pm-starmer-and-british-troops-in-london-7c1b264ae4f944b4990602ef4466ffcc"

"February 14","The art of the deal? Zelenskyy says a Ukraine-Russia agreement must come through Trump negotiations","Zelenskyy appealed to Trump’s dealmaker image to help negotiate peace.","https://apnews.com/article/trump-zelenskyy-munich-security-conference-ukraine-1feeba7df83c4cc241370180b3673677"

"August 18","Zelenskky’s attire comes up second time in Oval Office","Zelenskyy returned to the White House wearing a suit, avoiding past criticism.","https://apnews.com/video/zelenskkys-attire-comes-up-second-time-in-oval-office-304afdac8d084a449e112ec4f1570a7e"

"May 27","Zelenskyy says ‘Russia is counting on a prolonged war’","Zelenskyy said Russia is counting on a long war.","https://apnews.com/video/zelenskyy-says-russia-is-counting-on-a-prolonged-war-7391649a507c42729423a2933fca945f"

"April 28","Zelenskyy calls for stronger international pressure on Russia to end Ukraine war","Zelenskyy said Russia is “deceiving” the U.S. about peace intentions.","https://apnews.com/video/zelenskyy-calls-for-stronger-international-pressure-on-russia-to-end-ukraine-war-b34cd4671f1b4a99a0666a94f5b51ff5"

"August 6","Trump could meet in person with Putin as soon as next week, White House official says","Trump may meet Putin next week to discuss the war in Ukraine.","https://apnews.com/article/russia-ukraine-war-witkoff-moscow-trump-deadline-118b3cbcfa12d1dd9a75ce20b0b3e61e"

"August 5","Trump takes an unexpected walk on the White House roof to survey new projects","Trump appeared on the White House roof after a call with Zelenskyy.","https://apnews.com/article/trump-white-house-roof-west-wing-oval-b1e14afeea900df7858e7fd41e1578d0"

"May 15","The diplomatic road seeking peace in Ukraine has had twists and turns","European leaders met Zelenskyy to push Putin toward a ceasefire.","https://apnews.com/article/russia-ukraine-peace-talks-diplomacy-ceasefire-negotiations-adc1034f0eed21efcdbb35c9a68bde6c"

"July 23","Ukrainians are protesting a law targeting anti-corruption agencies. Here’s why","Ukrainians are protesting a new law they say undermines anti-corruption agencies.","https://apnews.com/article/ukraine-corruption-law-european-union-e4e1463a20555fe6db4ee7732fe1ab38"

"February 10","White House officials ready to meet with Zelenskyy in Munich for talks on Russia’s war on Ukraine","Trump’s senior advisers will meet Zelenskyy at Munich Security Conference.","https://apnews.com/article/ukraine-russia-war-zelenskyy-trump-kellogg-e38e0ec1a4c7e1e58b503c3831732ad0"

"November 30, 2024","Zelenskyy says NATO offer for Ukraine-controlled territory could end ‘hot stage’ of war","Zelenskyy said NATO membership for controlled territory could halt fighting.","https://apnews.com/article/russia-ukraine-war-zelenskyy-nato-92069fae6a05fc03d6fb2643ecbb4b2a"

"July 5","Ukraine says it struck a Russian air base as Russia sent hundreds of drones into Ukraine","Ukraine struck a Russian air base while Russia launched over 300 drones.","https://apnews.com/article/russia-ukraine-war-drones-airbase-trump-zelenskyy-d403d0807e35a64f530d587dbd218aa5"

"May 18","Ukraine’s leader meets with US and European officials ahead of high-stakes Trump-Putin call","Zelenskyy met top US and European officials ahead of a Trump–Putin call.","https://apnews.com/article/russia-ukraine-drone-attack-deadly-ceasefire-talks-b18d7ad72951680f24dbf289976c6251"

"March 27","Zelenskyy speaks on reasons behind delay of potential mineral deal with the US","Zelenskyy said negotiations on a mineral deal with the US keep changing.","https://apnews.com/video/zelenskyy-speaks-on-reasons-behind-delay-of-potential-mineral-deal-with-the-us-342a090790f3419ba0291074295dc027"

"January 3","Trump’s strength and unpredictability can help end the war in Ukraine, Zelenskyy says","Zelenskyy said Trump’s unpredictability could help end the war.","https://apnews.com/article/russia-ukraine-war-trump-zelenskyy-a80e4d3498692218f40a42bc3718c7c9"

"December 7, 2024","Ukraine confirms second Danish delivery of F-16s as Zelenskyy seeks support in Paris","Denmark delivered a second batch of F-16s as Zelenskyy sought support in Paris.","https://apnews.com/article/russia-ukraine-war-f16-denmark-86c2d6631869cc8f5217482e22bf52d8"

"October 18","Ukrainians express disappointment at possibility of not obtaining US Tomahawk missiles","Kyiv residents expressed disappointment after the US leaned against selling Tomahawk missiles.","https://apnews.com/video/ukrainians-express-disappointment-at-possibility-of-not-obtaining-us-tomahawk-missiles-c9af0a784c6e41c19214bd59e5c79e7d"

"January 25","US has not stopped military aid to Ukraine, Zelenskyy says","Zelenskyy said the US has not stopped military aid to Ukraine.","https://apnews.com/article/russia-ukraine-war-zelenskyy-us-aid-7a2d78db94565e6808e6d0699f6fa38d"

"April 26","Donald Trump and Volodymyr Zelenskyy hold talks in Vatican before funeral service for Pope"

"May 12","Zelenskyy says he would like to see Trump at Ukraine-Russia talks in Turkey",
"Zelenskyy says he wants Trump present at upcoming Ukraine-Russia talks in Ankara.",
"https://apnews.com/video/zelenskyy-says-he-would-like-to-see-trump-at-ukraine-russia-talks-in-turkey-78780c22242c4402ae588d914c9cad08"

"May 15","Zelenskyy slams Putin’s absence in Turkey for peace talks",
"Zelenskyy criticized Putin for refusing to attend the first direct Ukraine-Russia peace talks in 3 years.",
"https://apnews.com/video/zelenskyy-slams-putins-absence-in-turkey-for-peace-talks-ca04108b57f345a4babd66a4235a61d6"

"August 1","Kyiv mourns after deadliest attack in a year kills 31 people in Ukraine, including 5 children",
"Kyiv declared a day of mourning after Russia’s deadliest drone/missile attack in a year.",
"https://apnews.com/article/russia-ukraine-war-kyiv-attack-trump-putin-42474bc80c492190ec88861322ff0f84"

"August 16","Trump greets Putin with a red carpet. Ukrainians feel betrayed.",
"Ukrainians were stunned after Trump welcomed Putin on a red carpet in Alaska.",
"https://apnews.com/article/russia-ukraine-war-reactions-100265432874d44f93cbd8b337f69020"

"April 20","Faithful gather at church ruins on Easter in Ukraine, as Zelenskyy urges people not to lose faith",
"Ukrainian Christians gathered in ruined churches as Zelenskyy urged people not to lose faith.",
"https://apnews.com/video/faithful-gather-at-church-ruins-on-easter-in-ukraine-as-zelenskyy-urges-people-not-to-lose-faith-4dfb5eace2db40fe8150cbb8b6d8d928"

"February 1","AP Interview: Zelenskyy says excluding Ukraine from US-Russia talks about war is ‘very dangerous’",
"Zelenskyy said excluding Ukraine from US-Russia talks would be 'very dangerous'.",
"https://apnews.com/article/russia-ukraine-war-trump-talks-ceasefire-00af5f61f1faf41e78a3b4e072c21a14"

"May 13","Zelenskyy says he will be waiting for Putin in Turkey on Thursday for talks and that Trump invited",
"Zelenskyy said he will be waiting in Ankara for face-to-face talks with Putin.",
"https://apnews.com/video/zelenskyy-says-he-will-be-waiting-for-putin-in-turkey-on-thursday-for-talks-and-that-trump-invited-95fe2e72cfad4146b41e5d3358184fd3"

"March 2","Ukrainian soldiers reflect on Zelenskyy-Trump row in the Oval Office",
"Ukrainian soldiers said fighting without US support will be 'very hard' after the Zelenskyy-Trump row.",
"https://apnews.com/video/ukrainian-soldiers-reflect-on-zelenskyy-trump-row-in-the-oval-office-365114c9237345ccac17e7c9d363b278"

"April 16","Zelenskyy praises ‘good results’ in talks with US on mineral agreement",
"Zelenskyy said Ukraine achieved 'good results' in mineral agreement negotiations with the US.",
"https://apnews.com/video/zelenskyy-praises-good-results-in-talks-with-us-on-mineral-agreement-803dfde724df42eeab2e7d0689bd660a"

"May 6","Zelenskyy welcomes back released Ukrainian POWs after latest swap with Russia",
"Zelenskyy welcomed home hundreds of freed Ukrainian POWs in one of the largest swaps since 2022.",
"https://apnews.com/video/zelenskyy-welcomes-back-released-ukrainian-pows-after-latest-swap-with-russia-3adbfb80cc004508a91abbdac0c93874"

"June 17","Zelenskyy describes a ‘very difficult night’ under Russian bombardment as Canada promises more aid",
"Zelenskyy described a severe Russian bombardment while seeking support at the G7 summit.",
"https://apnews.com/video/zelenskyy-describes-a-very-difficult-night-under-russian-bombardment-as-canada-promises-more-aid-f0cef5c15b4d4a10a3a119575b892da2"

"October 24","UK Prime Minister welcomes Ukrainian president at Downing Street",
"UK PM Starmer welcomed Zelenskyy before he met European leaders in London.",
"https://apnews.com/video/uk-prime-minister-welcomes-ukrainian-president-at-downing-street-5bdd299a078a40e2b56de2ca088f483b"

"April 17","Zelenskyy says he has information that China is supplying weapons to Russia",
"Zelenskyy said Ukraine received intelligence that China is supplying weapons to Russia.",
"https://apnews.com/video/zelenskyy-says-he-has-information-that-china-is-supplying-weapons-to-russia-05c4ac8d7db24552969aff1b4cbfe2ba"

"April 24","Zelenskyy and Ramaphosa hold meeting in presidential palace in Pretoria",
"Zelenskyy met South African President Ramaphosa at the presidential palace in Pretoria.",
"https://apnews.com/video/zelenskyy-and-ramaphosa-hold-meeting-in-presidential-palace-in-pretoria-c4e58e7ae4824fcea920202645e7ad19"

"May 18","JD Vance and Zelenskyy arrive for inaugural mass of Pope Leo XIV at the Vatican",
"JD Vance and Zelenskyy attended Pope Leo XIV's inaugural mass in Vatican City.",
"https://apnews.com/video/arrivals-for-the-investiture-mass-of-pope-leo-xiv-in-the-vatican-0271dabfbee04bec8cc6a21f5af7dae3"

"June 4","Zelenskyy aide in DC downplays Hegseth absence at Ukraine Defense Contact Group",
"Zelenskyy's chief of staff Andriy Yermak downplayed absence of U.S. Defense Chair Pete Hegseth.",
"https://apnews.com/video/zelenskyy-aide-in-dc-downplays-hegseth-absence-at-ukraine-defense-contact-group-587f75a881324289a512dfee72184e16"

"July 26","4 people killed, multiple others injured in Russia and Ukraine as they trade aerial attacks",
"Russia and Ukraine traded aerial attacks overnight; 4 killed in both countries.",
"https://apnews.com/article/russia-ukraine-war-drone-attack-casualties-48d82c95b076c93a623e20e71366f241"

"March 23","Ukrainian President Zelenskyy visits the frontline in Kharkiv",
"Zelenskyy visited frontline defensive installations in the Kharkiv region.",
"https://apnews.com/video/ukrainian-president-zelenskyy-visits-frontline-in-kharkiv-20973d66a32444419609a4e629f0d107"

"May 18","Pope Leo XIV meets Ukrainian President Zelenskyy and Peruvian President Boluarte",
"Pope Leo XIV met Zelenskyy and Peru’s president after his inaugural mass.",
"https://apnews.com/video/pope-leo-xiv-meets-ukrainian-president-zelenskyy-and-peruvian-president-boluarte-2cd87fe075d945abbd4faf98db36030a"

"March 3","How Trump’s history with Russia and Ukraine set the stage for a blowup with Zelenskyy",
"Context on Trump’s past with Russia and Ukraine ahead of his blowup with Zelenskyy.",
"https://apnews.com/article/trump-russia-ukraine-fbi-mueller-ff6d60923de68632f2671e275083b54b"

"May 15","Zelenskyy and Russian delegation arrive in Turkey for peace talks",
"Zelenskyy accused Russia of sending a ‘decorative level’ delegation to peace talks in Ankara.",
"https://apnews.com/video/zelenskyy-and-russian-delegation-arrive-in-turkey-for-peace-talks-0ca1a85635b94cf689199ec4c6a300a2"

"May 12","Russian drones attack Ukraine after Kremlin rejects ceasefire proposal but promises talks",
"Russia launched over 100 drones after rejecting a Ukrainian ceasefire proposal.",
"https://apnews.com/article/russia-ukraine-war-ceasefire-peace-talks-e9f4832b8cbae8c40f4cfed3de3c678f"

"April 13","Zelenskyy issues strongly worded condemnation of Russia over deadly Sumy attack",
"Zelenskyy condemned Russia's deadly missile strike on Sumy.",
"https://apnews.com/video/zelenskyy-issues-strongly-worded-condemnation-of-russia-over-deadly-sumy-attack-ffcdc43435954c3889457732573fb28a"

"April 14","Zelenskyy calls for increased pressure on Russia following deadly missile attack on Sumy",
"Zelenskyy called for higher pressure on Russia after the Palm Sunday attack on Sumy.",
"https://apnews.com/video/zelenskyy-calls-for-increased-pressure-on-russia-following-deadly-missile-attack-on-sumy-0cc1b30e0e4e491ab0a52bf0528a29a1"

"June 4","Zelenskyy rejects Russia’s peace proposal, wants face-to-face talks with Putin",
"Zelenskyy rejected Russia’s peace plan and insisted on direct talks with Putin.",
"https://apnews.com/video/zelenskyy-rejects-russias-peace-proposal-wants-face-to-face-talks-with-putin-98e344f9eb9443dbb82626b05b6b14a9"

"July 15","Ukrainians welcome US aid but see Trump’s 50-day ultimatum to Putin as too long",
"Zelenskyy thanked Trump for new U.S. weapons, especially Patriot systems.",
"https://apnews.com/article/ukraine-trump-support-tariffs-russia-delay-9b620082c8fe3c457b23b0fe01241da2"

"February 1","Takeaways from the AP interview with Ukraine’s Zelenskyy",
"Key takeaways from AP’s exclusive interview with Zelenskyy.",
"https://apnews.com/article/russia-ukraine-war-trump-talks-ceasefire-08d77c7f2ca8ac07e74baf0d6ceff33a"

"March 20","President Zelenskyy says all of Ukraine’s power plants ‘belong to the people’",
"Zelenskyy emphasized that all Ukrainian power plants belong to the people.",
"https://apnews.com/video/president-zelenskyy-says-all-of-ukraines-power-plants-belong-to-the-people-b4033652f1de47818604469de8bfe60b"

"May 28","Merz says Germany will increase its support to Ukraine after meeting with Zelenskyy in Berlin",
"Germany’s Chancellor Merz pledged increased Ukraine support after meeting Zelenskyy.",
"https://apnews.com/video/merz-says-germany-will-increase-its-support-to-ukraine-after-meeting-with-zelenskyy-in-berlin-fcf0298f4bb9489cab4bccf42df9720e"

"June 1","Zelenskyy praises Ukraine’s Security Service for ‘brilliant operation’ in Russian territory",
"Zelenskyy praised Ukrainian intelligence for a ‘brilliant’ cross-border operation.",
"https://apnews.com/video/zelenskyy-praises-ukraines-security-service-for-brilliant-operation-in-russian-territory-cfff3b6de6974e859bcafe627902f62c"
"May 11","Zelenskyy hopes for ceasefire with Russia and challenges Putin to meet him in Turkey ‘personally’",
"Zelenskyy challenged Vladimir Putin to meet him personally in Turkey during upcoming talks.",
"https://apnews.com/video/zelenskyy-hopes-for-ceasefire-with-russia-and-challenges-putin-to-meet-him-in-turkey-personally-30c46105f2154574a2c847bcca123f3a"

"March 3","Polish democracy hero Wałęsa says Trump’s treatment of Zelenskyy filled him with ‘horror’",
"Lech Wałęsa and 38 former political prisoners said Trump's Oval Office treatment of Zelenskyy filled them with horror.",
"https://apnews.com/article/poland-trump-walesa-ukraine-russia-eab6a26169183760c844580f7742fd78"

"May 1","Zelenskyy says minerals deal with the US is a ‘truly equal agreement’",
"Zelenskyy said a negotiated minerals deal with the US was a 'truly equal agreement.'",
"https://apnews.com/video/zelenskyy-says-minerals-deal-with-the-us-is-a-truly-equal-agreement-27f48903abc84677a78a96e15cadda01"

"July 11","US is selling weapons to NATO allies to give to Ukraine, Trump says",
"Trump said the US is selling weapons to NATO allies so they can send them to Ukraine.",
"https://apnews.com/article/russia-ukraine-war-zelenskyy-trump-drones-05ba74cd9fbefcd81cc90886d091af5a"

"May 14","As eyes turn toward Turkey, here’s what to know about Russia-Ukraine peace talks",
"A guide to upcoming Russia–Ukraine peace talks across multiple capitals.",
"https://apnews.com/article/russia-ukraine-war-istanbul-peace-talks-putin-54e7e2b93df0c53712f1b8ce7248e824"

"March 1","Trump’s Oval Office thrashing of Zelenskyy shows limits of Western allies’ ability to sway US leader",
"Trump’s Oval Office confrontation with Zelenskyy exposed allies’ limits in shaping Trump’s stance on the war.",
"https://apnews.com/article/trump-zelenskyy-oval-office-ukraine-russia-blowup-8aa63e55c859e8fea963911478c376ee"

"February 6","Zelenskyy to lead Ukraine’s delegation at Munich Security Conference which JD Vance will attend",
"Zelenskyy will lead Ukraine’s delegation at Munich Security Conference.",
"https://apnews.com/article/ukraine-russia-war-15a42b01bd87e1bef5bd40ae5c910280"

"February 16","US presented Ukraine with a document to access its minerals but offered almost nothing in return",
"Zelenskyy said he told ministers not to sign a US minerals deal that heavily favored American interests.",
"https://apnews.com/article/ukraine-us-zelenskyy-agreement-trump-minerals-4d5eefcc44c9f17f330db98d81720b29"

"March 10","Saudi Crown Prince Mohammed Bin Salman receives Ukraine President Zelenskyy in Jeddah",
"Zelenskyy arrived in Jeddah for talks with Saudi leaders and the US Secretary of State.",
"https://apnews.com/video/saudi-crown-prince-mohammed-bin-salman-receives-ukraine-president-zelenskyy-in-jeddah-53c708a9fcf543b9b1b322edbc3493fa"

"February 23","Zelenskyy responds to Trump calling him a ‘dictator’",
"Zelenskyy said he does not recognize US aid as debt and criticized Trump’s remarks.",
"https://apnews.com/video/zelenskyy-comments-on-us-aid-and-trump-dictator-remarks-0606e29997674cca8d748a22de0c10f4"

"March 3","Trudeau reiterates support for Zelenskyy after Oval Office blowout",
"Canadian PM Trudeau reaffirmed support for Zelenskyy after Trump lashed out at him.",
"https://apnews.com/video/trudeau-reiterates-support-for-zelenskyy-after-oval-office-blowout-440afa8c7a554728895fdbe2f033d387"

"April 29","Zelenskyy suggests Russia might be preparing a new attack, using military drills in Belarus as cover",
"Zelenskyy warned that Russian drills in Belarus may conceal preparations for a new attack.",
"https://apnews.com/video/zelenskyy-suggests-russia-might-be-preparing-a-new-attack-using-military-drills-in-belarus-as-cover-1e6c6e6f082c4b24a028449c2adef9b9"

"September 30","At least 10 people injured in Russian drone strike on Ukrainian city of Dnipro",
"Ten people were injured in a Russian drone strike on Dnipro.",
"https://apnews.com/video/at-least-10-people-injured-in-russian-drone-strike-on-ukrainian-city-of-dnipro-ed0f768aa83b49c4950e9705c3710872"

"May 19","Zelenskyy discusses call with Trump as US says Russia-Ukraine truce talks to begin ‘immediately’",
"Zelenskyy urged Trump not to make decisions about Ukraine without Kyiv’s input.",
"https://apnews.com/video/zelenskyy-discusses-call-with-trump-as-us-says-russia-ukraine-truce-talks-to-begin-immediately-7ce82b9cd95a44198d3ac6e61aa4a054"

"February 26","Trump says Zelenskyy is coming to the White House to sign US-Ukraine critical minerals deal",
"Trump said Zelenskyy will visit the White House to sign a major minerals deal.",
"https://apnews.com/article/russia-ukraine-war-trump-economic-deal-faf1ff881802c923370053e539ec26e4"

"March 4","Rep. Chip Roy weighs in on Zelenskyy’s approach to US relations",
"Rep. Chip Roy spoke about Zelenskyy’s approach to U.S. relations in Congress.",
"https://apnews.com/video/rep-chip-roy-weighs-in-on-zelenskyys-approach-to-us-relations-000001956372d0d8a5f57b7ec8e60000"

"April 24","Ukraine’s Zelenskyy says Russia is putting pressure on US",
"Zelenskyy said Russia is pressuring the U.S., speaking during a visit to South Africa.",
"https://apnews.com/video/ukraines-zelenskyy-says-russia-is-putting-pressure-on-us-b89fb4611f524acb9d0bcf3b4b1cc129"

"May 3","Russia and Ukraine clash over ceasefire proposals as fighting rages",
"Ukraine and Russia clashed over competing ceasefire proposals.",
"https://apnews.com/article/russia-ukraine-war-drones-kharkiv-4396be6394f46a6320cac4bf82be2941"

"April 24","Trump says ‘it’s been harder’ to deal with Zelenskyy than Russia",
"Trump said Zelenskyy has been more difficult to deal with than Russia.",
"https://apnews.com/video/trump-its-been-harder-to-deal-with-zelenskyy-than-russia-365aeca3d38642f98e430efcc33f3db2"

"July 16","Russian attack targeting Ukraine’s energy infrastructure injures at least 15",
"Russia launched overnight attacks on four Ukrainian cities.",
"https://apnews.com/article/russia-ukraine-attack-trump-ultimatum-50-days-7388ae351bc78e42c9ab844be6b93942"

"September 23","Trump says NATO countries should shoot down Russian aircraft that violate their airspace",
"Trump said NATO should down Russian aircraft violating airspace.",
"https://apnews.com/video/trump-says-nato-countries-should-shoot-down-russian-aircraft-that-violate-their-airspace-9c9a8ac16e244c8ba6711246e4a03d21"

"April 22","Zelenskyy, Catholics gather in Kyiv, offer condolences on the passing of Pope Francis",
"Zelenskyy expressed condolences to Ukrainian religious leaders after Pope Francis’ death.",
"https://apnews.com/video/zelenskyy-catholics-gather-in-kyiv-offers-condolences-on-the-passing-of-pope-francis-90546286f84d4366a2a1516fb0961414"

"March 18","Ukrainian President Zelenskyy calls for pressure to be put on Moscow to accept ceasefire proposal",
"Zelenskyy urged pressure on Moscow to accept the US-backed ceasefire plan.",
"https://apnews.com/video/ukrainian-president-zelenskyy-calls-for-pressure-to-be-put-on-moscow-to-accept-ceasefire-proposal-f309264a2cba403dada519089f880bbd"

"March 31","Ukraine hasn’t held elections since Russia’s full-scale invasion. Here’s why",
"Ukraine suspended elections due to wartime conditions, extending Zelenskyy’s term.",
"https://apnews.com/article/ukraine-elections-timing-war-zelenskyy-critics-f4f810d810ffc3cf4c81b241bbd76dac"

"July 9","Russia batters Ukraine with more than 700 drones, the largest barrage of the war",
"Russia launched over 700 drones in one night, the largest attack so far.",
"https://apnews.com/article/russia-record-drone-attack-ukraine-war-fe3d23673b9b5696bb5097def9ed0775"

"April 27","Trump says Zelenskyy asked for more weapons at Vatican meeting and was ready to give up Crimea",
"Trump claimed Zelenskyy wanted more weapons and was open to conceding Crimea.",
"https://apnews.com/video/trump-says-zelenskyy-asked-for-more-weapons-at-vatican-meeting-and-was-ready-to-give-up-crimea-97414cfeb3014f91a676d5719318d437"


"March 25","Zelenskyy on talks between the US and ‘the war team’ in Saudi Arabia",
"Zelenskyy commented on US–Russia talks in Saudi Arabia.",
"https://apnews"

"""

def title_contains_zelensky(title: str) -> bool:
    """判断标题是否包含 Zelensky / Zelenskyy / 泽连斯基"""
    if not isinstance(title, str):
        return False
    title_lower = title.lower()
    return (
        "zelenskyy" in title_lower
        or "zelensky" in title_lower
        or "泽连斯基" in title_lower
    )

def main():
    # 将文本读成 CSV DataFrame
    df = pd.read_csv(
        StringIO(csv_text_ap),
        header=None,
        names=["date", "title", "short_opening", "url"]
    )
    
    # 过滤只含泽连斯基的标题
    filtered = df[df["title"].apply(title_contains_zelensky)]

    # 去重（按 URL 去）
    filtered = filtered.drop_duplicates(subset=["url"])

    # 输出
    out_file = "zelensky_ap_notfiltered.csv"
    filtered.to_csv(out_file, index=False)

    print(f"生成完成：{out_file}（共 {len(filtered)} 条）")

if __name__ == "__main__":
    main()
