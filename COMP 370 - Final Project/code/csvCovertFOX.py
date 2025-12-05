import pandas as pd

rows = []

# 把我给你的全部 CSV 文本黏贴进这里
csv_text = """ date,title,short_opening,url
"February 28","Trump, Vance and Zelenskyy spar over Russian war in tense exchange: 'Very disrespectful'","President Donald Trump, Vice President JD Vance and Ukraine President Volodymyr Zelenskyy sparred during a meeting at the White House to end the Russia-Ukraine War.","https://www.foxnews.com/politics/trump-vance-zelenskyy-spar-over-russian-war-tense-exchange-very-disrespectful"

"2 days ago","Zelenskyy moves to 'clean up' Ukraine's energy sector as corruption scandal rocks leadership","Ukrainian President Volodymyr Zelenskyy announced major energy sector cleanup Sunday as corruption scandal rocks the nation's nuclear industry.","https://www.foxnews.com/politics/zelenskyy-moves-clean-up-ukraines-energy-sector-corruption-scandal-rocks-leadership"

"February 28","Tulsi Gabbard thanks Trump for 'unwavering leadership' in Oval Office clash with Zelenskyy","Tulsi Gabbard commended President Trump's 'unwavering leadership' after a controversial dustup with Ukrainian President Volodymyr Zelenskyy.","https://www.foxnews.com/politics/tulsi-gabbard-thanks-trump-unwavering-leadership-oval-office-clash-zelenskyy"

"February 17","Zelenskyy not yet signing US economic agreement 'short-sighted,' White House official says","A White House national security official said Ukrainian President Volodymyr Zelenskyy 'is being short-sighted' in not signing a rare earth minerals deal.","https://www.foxnews.com/world/zelenskyy-not-yet-signing-us-economic-agreement-short-sighted-white-house-official-says"

"August 17","European leaders will join Trump-Zelenskyy meeting, signaling solidarity with Ukraine","European leaders including France's Macron and UK's Starmer join Zelenskyy for crucial Washington meeting with Trump.","https://www.foxnews.com/politics/european-leaders-join-trump-zelensky-meeting-signaling-solidarity-ukraine"

"August 17","European leaders will join Trump-Zelenskyy meeting, signaling solidarity with Ukraine","European leaders including France's Macron and UK's Starmer join Zelenskyy for crucial Washington meeting with Trump.","https://www.foxnews.com/politics/european-leaders-join-trump-zelensky-meeting-signaling-solidarity-ukraine"

"February 18","Zelenskyy faces perilous re-election odds as US, Russia push Ukraine to go to the polls","U.S. and Russia push Ukraine to hold elections as Zelenskyy's term is past expiration.","https://www.foxnews.com/politics/zelenskyy-faces-perilous-reelection-odds-us-russia-push-ukraine-go-polls-part-peace-deal"

"5 days ago","Top Ukrainian officials in Zelenskyy government submit resignations amid $100 million corruption scandal","Anti-corruption agencies expose alleged kickback scheme in Energoatom.","https://www.foxnews.com/world/top-ukrainian-officials-zelenskyy-government-submit-resignations-amid-100-million-corruption-scandal"

"February 3","Zelenskyy warns peace talks without Ukraine 'dangerous' after Trump claims meetings with Russia 'going well'","Zelenskyy warns Trump-led talks with Russia without Ukraine would be 'dangerous.'","https://www.foxnews.com/world/zelenskyy-warns-peace-talks-without-ukraine-dangerous-after-trump-claims-meetings-russia-going-well"

"July 6","Zelenskyy touts 'fruitful' Trump call after US president disappointed by Putin talk","Zelenskyy and Trump held a strategic call about air defense and Patriot missiles.","https://www.foxnews.com/world/zelenskyy-touts-fruitful-trump-call-after-us-president-disappointed-putin-talk"

"August 17","Ukrainian designer predicts Zelenskyy will wear military suit for high-stakes Trump meeting","Designer says Zelenskyy will likely choose military-style clothing for DC meeting.","https://www.foxnews.com/world/ukrainian-designer-predicts-zelenskyy-wear-military-suit-high-stakes-trump-meeting"

"August 18","Trump moves to broker Putin-Zelenskyy meeting following DC peace talks","Trump announces plans for trilateral meeting.","https://www.foxnews.com/politics/trump-arranges-putin-zelenskyy-meeting-after-calling-russian-president-amid-ukraine-talks-from-white-house"

"September 23, 2024","Zelenskyy warns Vance’s plan to give Russia seized land will lead to ‘global showdown’","Zelenskyy says Vance's proposal would trigger global war.","https://www.foxnews.com/world/zelenskyy-warns-vances-plan-ukrainian-lands-seized-russia-result-global-showdown"

"March 1","Zelenskyy meets with British Prime Minister Keir Starmer in London following Trump Oval Office clash","Zelenskyy welcomed by UK's PM after White House clash.","https://www.foxnews.com/world/zelenskyy-meets-british-prime-minister-keir-starmer-london-following-trump-oval-office-clash"

"March 4","Zelenskyy says Ukraine 'ready' for peace negotiations, calls Trump meeting 'regrettable'","Zelenskyy calls recent Trump meeting 'regrettable.'","https://www.foxnews.com/politics/zelenskyy-says-ukraine-ready-peace-negotiations-calls-trump-meeting-regrettable"

"September 16","Trump and Zelenskyy to meet as Poland pressures NATO on no fly zone over Ukraine","Possible Zelenskyy–Trump meeting during UN summit.","https://www.foxnews.com/world/trump-zelenskyy-meet-poland-pressures-nato-no-fly-zone-over-ukraine"

"August 19","Trump reflects on Ukraine peace talks, working toward Putin-Zelenskyy meeting","Trump discusses efforts to arrange peace meeting.","https://www.foxnews.com/video/6377075188112"

"February 25","Trump says minerals deal has been 'pretty much' negotiated with Zelenskyy","Zelenskyy agrees to terms of minerals deal allowing US access.","https://www.foxnews.com/world/trump-says-minerals-deal-has-been-pretty-much-negotiated-zelenskyy-meeting-slated-friday"

"March 1","Zelenskyy meets with British Prime Minister Keir Starmer in London following Trump Oval Office clash","Zelenskyy meets with UK PM after tense US meeting.","https://www.foxnews.com/world/zelenskyy-meets-british-prime-minister-keir-starmer-london-following-trump-oval-office-clash"

"February 28","Where Zelenskyy is headed following tense White House exchange with Trump, Vance","Zelenskyy left White House after tense exchange.","https://www.foxnews.com/politics/where-zelenskyy-headed-following-tense-white-house-exchange-trump-vance"

"September 25","Zelenskyy 'ready' to exit office if war ends, open to elections in ceasefire","Zelenskyy says peace is priority over second term.","https://www.foxnews.com/world/zelensky-ready-leave-office-when-ukraine-war-ends"

"September 23","Trump and Zelenskyy signal stronger ties after UN meeting","Zelenskyy: relationship with Trump is 'better than before.'","https://www.foxnews.com/politics/trump-zelenskyy-signal-stronger-ties-after-un-meeting-better-relations-than-before"

"July 17","Ukraine's Zelenskyy names new prime minister","Zelenskyy appoints new PM amid ongoing war.","https://www.foxnews.com/world/ukraines-zelenskyy-names-new-prime-minister-first-time-since-russias-war-began"

"March 27","Zelenskyy sensationally predicts Putin 'will die soon'","Zelenskyy claims Putin’s health is collapsing.","https://www.foxnews.com/world/zelenskyy-sensationally-predicts-putin-will-die-soon"

"February 27","Why Zelenskyy keeps pushing for Ukraine NATO membership","Zelenskyy insists NATO path still crucial.","https://www.foxnews.com/politics/why-zelenskyy-keeps-pushing-ukraine-nato-membership-even-though-trump-says-its-not-happening"

"August 19","Russia launches largest attack on Ukraine this month following Trump's meetings with Zelenskyy","Russia strikes Ukraine during Zelenskyy–Trump meetings.","https://www.foxnews.com/world/russia-launches-largest-attack-ukraine-month-following-trumps-meetings-putin-zelenskyy"

"February 28","Here's the real reason Trump and Zelenskyy's deal blew up in the Oval Office","Trump–Zelenskyy meeting exploded over lack of security guarantees.","https://www.foxnews.com/world/heres-real-reason-trump-zelenskyys-deal-blew-up-oval-office"

"February 28","Zelenskyy breaks silence on social media after fiery Oval Office exchange","Zelenskyy thanks America after tense White House clash.","https://www.foxnews.com/politics/zelenskyy-breaks-silence-social-media-after-fiery-oval-office-exchange-trump-thank-you-america"

"February 19","Trump calls Ukraine's Zelenskyy a 'dictator without elections'","Trump slams Zelenskyy after Saudi peace talks.","https://www.foxnews.com/politics/trump-calls-ukraines-zelenskyy-dictator-without-elections-rift-widens"

"August 17","'Our position is clear:' Zelenskyy and EU dismiss ceding Ukrainian land to Russia","Zelenskyy says Ukraine's constitution forbids territorial surrender.","https://www.foxnews.com/politics/our-position-clear-zelenskyy-eu-dismiss-ceding-ukrainian-land-russia"

"August 18","Russian drone strikes kill 7 in Kharkiv during Zelenskyy's White House meeting with Trump","Deadly drone attacks strike Kharkiv during Zelenskyy's DC visit.","https://www.foxnews.com/politics/russian-drone-strikes-kharkiv-during-zelenskyys-white-house-meeting-trump"

"May 6, 2022","Ukrainian President Zelenskyy to join virtual G7 summit","Zelenskyy set to join Biden and G7 leaders for virtual summit.","https://www.foxnews.com/politics/zelenskyy-join-virtual-g7-summit"

"4 days ago","Trump administration stays silent as massive Ukraine corruption scandal rocks Zelenskyy's inner circle","$100 million corruption scandal hits Zelenskyy administration.","https://www.foxnews.com/politics/trump-administration-stays-silent-massive-ukraine-corruption-scandal-rocks-zelenskys-inner-circle"

"May 18","Zelenskyy sheds details on meeting with Vance, Rubio in Rome after Russia peace talks stall","Zelenskyy discusses stalled Russia peace talks in Rome.","https://www.foxnews.com/politics/zelenskyy-slams-russia-sending-non-decision-makers-peace-talks-after-meeting-vance-rubio"

"February 25","Trump says minerals deal has been 'pretty much' negotiated with Zelenskyy","U.S. and Ukraine agree on mineral deal terms.","https://www.foxnews.com/world/trump-says-minerals-deal-has-been-pretty-much-negotiated-zelenskyy-meeting-slated-friday"

"September 24","Zelenskyy at UN: ‘Weak’ global bodies can’t stop Putin, only ‘friends and weapons’ can","Zelenskyy warns UN that Putin plans wider war.","https://www.foxnews.com/world/zelenskyy-un-weak-global-bodies-cant-stop-putin-only-friends-weapons-can"

"February 11","JD Vance, Treasury Sec Scott Bessent to meet with Zelenskyy as Trump team sets sights on Russia-Ukraine war","Vance to meet Zelenskyy amid shifting U.S. strategy.","https://www.foxnews.com/politics/jd-vance-treasury-sec-scott-bessent-meet-zelenskyy-trump-team-sets-sights-russia-ukraine-war"

"September 3","Putin invites Zelenskyy to a meeting in Moscow for security talks as he bombs Ukraine","Putin suggests meeting Zelenskyy despite ongoing attacks.","https://www.foxnews.com/world/putin-invites-zelenskyy-meeting-moscow-security-talks-as-he-bombs-ukraine"

"February 28","Furious Dems attack Trump, Vance after explosive Oval Office meeting with Zelenskyy","Democrats criticize Trump–Zelenskyy exchange as shameful.","https://www.foxnews.com/politics/furious-dems-attack-trump-vance-explosive-oval-office-meeting-zelenskyy-siding-dictators"

"August 7","Zelenskyy tells Putin to 'be brave' and finally agree to trilateral meeting with Trump","Zelenskyy pushes Putin for three-way peace meeting.","https://www.foxnews.com/world/zelenskyy-tells-putin-be-brave-finally-agree-trilateral-meeting-trump"

"February 24","Zelenskyy names his terms for giving up power as US, Ukraine lock in on mineral deal","Zelenskyy demands guarantees as Washington pressures him.","https://www.foxnews.com/politics/zelenskyy-names-his-terms-giving-up-power-us-ukraine-lock-mineral-deal-nato"

"February 26","Zelenskyy looking for ‘NATO or something similar’ as he prepares for meeting with Trump","Zelenskyy insists Ukraine needs NATO-level security guarantees.","https://www.foxnews.com/world/zelenskyy-looking-nato-something-similar-he-prepares-meeting-trump"

"March 2","Trump commerce secretary shreds Zelenskyy's security guarantee requests: 'Just ridiculous'","Commerce secretary rejects Zelenskyy's terms for peace deal.","https://www.foxnews.com/video/6369522376112"

"May 18","Zelenskyy sheds details on meeting with Vance, Rubio in Rome after Russia peace talks stall","Zelenskyy describes non-productive talks with Russia.","https://www.foxnews.com/politics/zelenskyy-slams-russia-sending-non-decision-makers-peace-talks-after-meeting-vance-rubio"

"February 25","Trump says minerals deal has been 'pretty much' negotiated with Zelenskyy","Mineral deal nearly finalized between U.S. and Ukraine.","https://www.foxnews.com/world/trump-says-minerals-deal-has-been-pretty-much-negotiated-zelenskyy-meeting-slated-friday"

"September 24","Zelenskyy at UN: ‘Weak’ global bodies can’t stop Putin, only ‘friends and weapons’ can","Zelenskyy says UN can't stop Putin alone.","https://www.foxnews.com/world/zelenskyy-un-weak-global-bodies-cant-stop-putin-only-friends-weapons-can"

"February 11","JD Vance, Treasury Sec Scott Bessent to meet with Zelenskyy","Vance plans meeting with Zelenskyy about war strategy.","https://www.foxnews.com/politics/jd-vance-treasury-sec-scott-bessent-meet-zelenskyy-trump-team-sets-sights-russia-ukraine-war"

"September 3","Putin invites Zelenskyy to a meeting in Moscow","Putin suggests Zelenskyy meet in Moscow amid escalation.","https://www.foxnews.com/world/putin-invites-zelenskyy-meeting-moscow-security-talks-as-he-bombs-ukraine"

"February 28","Furious Dems attack Trump, Vance after explosive Oval Office meeting with Zelenskyy","Dems slam Trump for clash with Zelenskyy.","https://www.foxnews.com/politics/furious-dems-attack-trump-vance-explosive-oval-office-meeting-zelenskyy-siding-dictators"

"August 7","Zelenskyy tells Putin to 'be brave' and finally agree to trilateral meeting","Zelenskyy challenges Putin to join peace talks.","https://www.foxnews.com/world/zelenskyy-tells-putin-be-brave-finally-agree-trilateral-meeting-trump"

"February 24","Zelenskyy names his terms for giving up power","Zelenskyy states conditions for stepping down.","https://www.foxnews.com/politics/zelenskyy-names-his-terms-giving-up-power-us-ukraine-lock-mineral-deal-nato"

"February 26","Zelenskyy looking for ‘NATO or something similar’","Zelenskyy urges allies for NATO-level security.","https://www.foxnews.com/world/zelenskyy-looking-nato-something-similar-he-prepares-meeting-trump"

"March 2","Trump commerce secretary shreds Zelenskyy's requests","Commerce official calls Zelenskyy's demands unreasonable.","https://www.foxnews.com/video/6369522376112"

"December 7","Trump meets with Macron, Zelenskyy ahead of Notre Dame reopening","Trump meets Zelenskyy and Macron in Paris.","https://www.foxnews.com/politics/trump-meets-macron-zelenskyy-notre-dame-ceremony-paris"

"October 17, 2024","Zelenskyy victory plan: Replace US troops with Ukrainians","Zelenskyy proposes replacing U.S. troops with Ukrainians across Europe.","https://www.foxnews.com/politics/zelensky-victory-plan-includes-replacing-us-troops-outposts-europe-battle-hardened-ukrainians"

"February 7","Trump plans to meet with Zelenskyy as he looks to end Ukraine war","Trump says Zelenskyy may visit DC soon.","https://www.foxnews.com/politics/trump-plans-meet-zelenskyy-he-looks-end-ukraine-war"

"March 7","Zelenskyy confirms Ukraine will attend US peace talks in Saudi Arabia","Zelenskyy confirms participation in US-led talks.","https://www.foxnews.com/world/zelenskyy-confirms-ukraine-attend-us-peace-talks-saudi-arabia-1-week-after-oval-office-clash"

"November 20","Zelenskyy answers whether he's willing to cede Crimea","Zelenskyy refuses to concede Ukrainian territory.","https://www.foxnews.com/world/zelenskyy-answers-whether-hes-willing-cede-crimea-other-territory-peace-deal"

"March 19","Zelenskyy wants details after Trump-Putin call, lays out 'red line' for Ukraine","Zelenskyy outlines Ukraine’s non-negotiable red line after Trump–Putin call.","https://www.foxnews.com/world/zelenskyy-wants-details-after-trump-putin-call-lays-out-red-line-ukraine"

"October 14, 2024","Harris' off-putting manner put Zelenskyy on defensive ahead of Russian invasion","Book reveals Harris put Zelenskyy on edge before Russia invasion.","https://www.foxnews.com/politics/harris-off-putting-manner-put-zelenskyy-defensive-ahead-russian-invasion-new-book-reveals"

"February 28","World leaders back Zelenskyy following Trump, Vance Oval Office spat","Leaders emphasize Russia is aggressor after Zelenskyy–Trump clash.","https://www.foxnews.com/world/world-leaders-back-zelenskyy-following-trump-vance-oval-office-spat"

"May 16","Zelenskyy speaks with Trump, allies after Russia peace talks broker no ceasefire","Zelenskyy and global leaders react to failed ceasefire talks.","https://www.foxnews.com/world/zelenskyy-speaks-trump-allies-after-russia-peace-talks-broker-no-ceasefire"

"September 7","Zelenskyy accuses Trump of giving Putin 'what he wanted' at Alaska summit","Zelenskyy criticizes Trump–Putin summit outcome.","https://www.foxnews.com/media/zelenskyy-accuses-trump-giving-putin-what-he-wanted-alaska-summit"

"May 11","Zelenskyy agrees to meet with Putin on Thursday","Zelenskyy accepts Putin’s proposal for high-stakes meeting.","https://www.foxnews.com/world/zelenskyy-agrees-meet-putin-thursday"

"October 17","Trump says 'tremendous bad blood' between Zelenskyy, Putin delaying peace deal","Trump blames Zelenskyy–Putin animosity for stalled peace deal.","https://www.foxnews.com/politics/trump-says-tremendous-bad-blood-between-zelenskyy-putin-delaying-peace-deal-despite-middle-east-momentum-"

"August 12, 2022","Ukrainian President Zelenskyy will soon have his own action figure","Action figure of Zelenskyy raises $139,000 in crowdfunding.","https://www.foxnews.com/lifestyle/ukraine-president-zelenskyy-action-figure"

"August 6","Trump open to meet Putin face-to-face next week followed by three-way talks with Zelenskyy","Trump schedules meetings with Putin and Zelenskyy.","https://www.foxnews.com/politics/trump-announces-face-face-talks-putin-next-week-three-way-talks-ukraines-zelenskyy"

"October 22","Trump meets NATO’s Rutte amid canceled Putin meeting: 'It didn't feel right to me'","Trump meets NATO chief after Zelenskyy White House visit.","https://www.foxnews.com/politics/trump-meets-natos-rutte-amid-canceled-putin-meeting-it-didnt-feel-right-me"

"August 15","Key takeaways from Trump-Putin summit as meeting with Zelenskyy might be next","Zelenskyy likely next in diplomatic sequence after Alaska summit.","https://www.foxnews.com/world/key-takeaways-from-trump-putin-summit-meeting-zelenskyy-might-next"

"September 25","Zelenskyy tells Kremlin leaders they should 'know where the bomb shelters are'","Zelenskyy warns Moscow officials amid escalation.","https://www.foxnews.com/world/zelenskyy-tells-kremlin-leaders-should-know-where-bomb-shelters-ominous-warning"

"August 18","5 key moments inside Trump’s ‘big day’ with Zelenskyy, European leaders","Zelenskyy–Trump meeting highlighted as major diplomatic moment.","https://www.foxnews.com/politics/key-moments-inside-trumps-big-day-zelenskyy-european-leaders"

"February 28","'Utter disaster': Lindsey Graham calls for Zelenskyy resignation after White House throwdown","Graham slams Zelenskyy, says he should resign or change.","https://www.foxnews.com/politics/utter-disaster-lindsey-graham-calls-zelenskyy-resignation-after-white-house-throwdown"

"February 27","Trump says 'I can't believe I said that' when asked if he still thinks Zelenskyy is a dictator","Trump dodges Zelenskyy dictator remark during meeting with Starmer.","https://www.foxnews.com/politics/trump-cant-believe-said-that-when-asked-thinks-zelenskyy-dictator"

"August 19","White House announces Putin agreed to bilateral meeting with Zelenskyy","Putin agrees to meet Zelenskyy one-on-one, per White House.","https://www.foxnews.com/politics/white-house-announces-putin-agreed-bilateral-meeting-zelenskyy"

"June 25","Zelenskyy pointedly thanks Trump, America for Ukraine support","Zelenskyy emphasizes gratitude months after tense exchange.","https://www.foxnews.com/politics/zelenskyy-pointedly-thanks-trump-america-ukraine-support-months-after-vances-jab-about-lack-gratitude"

"March 3","UK prime minister lays out Ukraine peace deal framework as Zelenskyy responds to resignation calls","Zelenskyy faces calls to resign while UK outlines plan.","https://www.foxnews.com/politics/uk-prime-minister-lays-out-ukraine-peace-deal-framework-zelenskyy-responds-resignation-calls"

"August 7, 2023","Ukraine arrests woman in alleged foiled Russian assassination plot against Zelenskyy","Ukraine arrests woman tied to Russian plot to assassinate Zelenskyy.","https://www.foxnews.com/world/ukraine-arrests-woman-alleged-foiled-russian-assassination-plot-against-zelenskyy"

"February 28","Who could lead Ukraine if Zelenskyy resigns?","Uncertainty looms over Ukrainian leadership if Zelenskyy steps down.","https://www.foxnews.com/world/who-could-lead-zelenskyy-resigned"

"February 28","World leaders back Zelenskyy following Trump, Vance Oval Office spat","Global leaders reaffirm support for Zelenskyy.","https://www.foxnews.com/world/world-leaders-back-zelenskyy-following-trump-vance-oval-office-spat"

"January 23","Trump says Zelenskyy is ‘no angel’","Trump discusses Zelenskyy and relationships with global leaders.","https://www.foxnews.com/video/6367602293112"

"November 5, 2024","Ukraine, North Korean troops clash for first time; Zelenskyy warns of escalation","Zelenskyy warns of escalating conflict as NK troops join Russia.","https://www.foxnews.com/world/ukraine-north-korean-troops-clash-first-time-zelenskyy-warns-escalation"

"February 28","SCOOP: GOP Ukraine supporters alarmed after explosive Trump, Zelenskyy meeting","GOP lawmakers shocked by tense Trump–Zelenskyy meeting.","https://www.foxnews.com/politics/scoop-gop-ukraine-supporters-alarmed-after-explosive-trump-zelenskyy-meeting"

"February 28","Zelenskyy says ire with Trump began with pro-Putin rhetoric","Zelenskyy says Trump's pro-Putin comments sparked tensions.","https://www.foxnews.com/world/zelenskyy-says-ire-trump-began-pro-putin-rhetoric"

"March 4","Fox News' Zelenskyy interview watched by 6.4 million viewers","Baier interview with Zelenskyy surpasses major networks.","https://www.foxnews.com/media/fox-news-zelenskyy-interview-watched-6-4-million-viewers-surpassing-nbc-cbs-evening-newscasts"

"June 8","Zelenskyy dismisses Trump's claim that Russia wants peace","Zelenskyy says he knows Putin better than Trump does.","https://www.foxnews.com/politics/zelenskyy-dismisses-trumps-claim-russia-wants-peace-says-he-knows-putin-much-better"

"November 26","Ukraine's Zelenskyy ordered missile strikes into Russia hours after trip to front lines","Zelenskyy orders strikes on Russia following frontline visit.","https://www.foxnews.com/world/ukraine-president-zelenskyy-ordered-missile-strikes-russia-hours-after-trip-front-lines-fox-news"

"March 30","Trump says Zelenskyy wants to back out of mineral deal","Trump says Zelenskyy reconsidering rare earth deal.","https://www.foxnews.com/politics/trump-says-zelenskyy-wants-back-out-mineral-deal-addresses-3rd-term-during-gaggle"

"February 19","Trump and Zelenskyy war of words heats up","Zelenskyy accuses Trump of spreading Russian disinformation.","https://www.foxnews.com/politics/trump-zelenskyy-war-words-heats-up-even-us-looks-wind-down-war-ukraine"

"February 14","Ukraine blames Russia for drone attack on Chernobyl's protective shell, Zelenskyy says damage 'significant'","Zelenskyy says drone strike caused significant damage to Chernobyl protective shell.","https://www.foxnews.com/world/ukraine-blames-russia-drone-attack-chernobyls-protective-shell-zelenskyy-says-damage-significant"

"October 11, 2022","Ukraine's Zelenskyy pushes 'peace formula' in G7 meeting, says 'no dialogue' with Putin","Zelenskyy presents peace formula and rules out dialogue with Putin.","https://www.foxnews.com/world/ukraine-zelenskyy-pushes-peace-formula-g7-meeting-says-no-dialogue-putin"

"March 17, 2022","Volodymyr Zelenskyy, 'the Churchill of our time': Reporter's Notebook","Zelenskyy portrayed as modern Churchill amid plea for weapons.","https://www.foxnews.com/politics/volodymyr-zelenskyy-churchill-our-time"

"October 17","Zelenskyy pitches Trump on Ukraine drone-for-Tomahawk missile exchange","Zelenskyy proposes drone-for-Tomahawk deal; Trump hesitant.","https://www.foxnews.com/world/zelenskyy-pitches-trump-ukraine-drone-for-tomahawk-missile-exchange-president-weighs-escalation-concerns"

"February 28","Zelenskyy says ire with Trump began with pro-Putin rhetoric","Zelenskyy says Trump's comments triggered public distrust.","https://www.foxnews.com/world/zelenskyy-says-ire-trump-began-pro-putin-rhetoric"


"""
### 以下是 AP News 的 CSV 文本
csv_text_ap = """ 
"2 hours ago","Russian attack kills 25 in Ukraine’s Ternopil as Zelenskyy meets Erdogan in Turkey","A Russian drone and missile attack on Ukraine’s western city of Ternopil has killed at least 25 people, including three children.","https://apnews.com/article/russia-ukraine-war-drone-missile-attack-a8c310e868905ea8905334ffb3869fcb"
"3 hours ago","Top Ukrainian ministers submit their resignations as the country is rocked by a corruption scandal","Ukraine’s justice and energy ministers submitted their resignations amid a major embezzlement and kickbacks scandal involving the state nuclear power company.","https://apnews.com/article/russia-ukraine-war-corruption-scandal-6e33b63b8071f46140956d4d23ab00de"
"November 17","Ukraine plans to buy up to 100 Rafale warplanes and air defense systems from France","Ukraine has signed a letter of intent to buy up to 100 Rafale warplanes from France, along with drones and ground-to-air systems.","https://apnews.com/article/france-ukraine-warplanes-rafale-1ac56c0377a9d40fd28462df1b1acd63"
"September 24","Macron and Zelenskyy hold bilateral meeting at the United Nations","French President Emmanuel Macron and Ukrainian President Volodymyr Zelenskyy held a bilateral meeting on the sidelines of the UN General Assembly on Wednesday.","https://apnews.com/video/macron-and-zelensky-hold-bilateral-meeting-at-the-united-nations-d25c943c7c194a0eb1b0c65a9ffb20ee"
"August 19","US troops won’t be sent to help defend Ukraine, Trump says","President Donald Trump is offering his assurances that U.S. troops won’t be sent to help defend Ukraine against Russia.","https://apnews.com/article/trump-russia-ukraine-war-defend-american-troops-85704282576324a36567798e9cb741ec"
"August 18","Takeaways from Trump’s meeting with Zelenskyy and Europeans: Praise, security talks, more meetings","President Donald Trump says the U.S. could support a European force in Ukraine to maintain a lasting peace in Russia’s war.","https://apnews.com/article/russia-ukraine-war-trump-zelensky-what-to-know-f70e7c231251f263a66772d954eefff5"
"August 18","European leaders join Trump and Zelenskyy for critical talks on ending Russia’s war in Ukraine","A group of European leaders joined Ukrainian President Volodymyr Zelenskyy and President Donald Trump for critical talks at the White House.","https://apnews.com/video/european-leaders-join-trump-and-zelensky-for-critical-talks-on-ending-russias-war-in-ukraine-9f943d0404dc49fbacf884cfbd1d0afe"
"August 18","Zelenskyy arrives at White House, meeting with Trump and European leaders.","The U.S. president welcomed the Ukrainian leader at the door of the West Wing.","https://apnews.com/video/zelenskyy-arrives-at-white-house-meeting-with-trump-and-european-leaders-77855e091de942028c277d8c622471a1"
"August 7","Trump says he would meet with Putin even if the Russian leader won’t meet with Ukraine’s Zelenskyy","President Donald Trump said Thursday he would meet with Vladimir Putin even if the Russian leader won’t meet with Ukrainian President Volodymyr Zelensky.","https://apnews.com/video/trump-says-he-would-meet-with-putin-even-if-the-russian-leader-wont-meet-with-ukraines-zelenskyy-6fd11ec4c07e45638b889bc3f5b60e05"
"May 13","At Cannes opening, Robert De Niro calls Trump ‘America’s philistine president’","Much of the cinema world descended on the Cannes Film Festival as the 78th edition got underway.","https://apnews.com/article/cannes-film-festival-opening-robert-de-niro-035fd29f2b532f26c2e55e5729ae5998"
"May 6","Zelenskyy welcomes back released Ukrainian POWs after latest swap with Russia","Zelenskyy celebrated the release of hundreds of captured Ukrainian soldiers in one of the largest swaps since 2022.","https://apnews.com/video/zelenskyy-welcomes-back-released-ukrainian-pows-after-latest-swap-with-russia-3adbfb80cc004508a91abbdac0c93874"
"April 29","If Trump abandons Ukraine, can Europe help Kyiv fight on? The clock is ticking to answer that","Trump is pushing Zelensky to cede territory to Russia to end the war.","https://apnews.com/article/ukraine-europe-trump-defense-putin-zelenskyy-862fe7f477d372024d22cb74508adf6f"
"April 25","Trump calls for Ukraine and Russia to meet for ‘very high level’ talks, says they are close to deal","President Donald Trump says the sides are “very close to a deal” after productive meetings.","https://apnews.com/article/russia-ukraine-war-trump-putin-33015fe967ab7cd09fee165fed59953e"
"April 14","Russia claims its deadly attack on Ukraine’s Sumy targeted military forces as condemnation grows","Russia claims its missile strike targeted a gathering of Ukrainian troops.","https://apnews.com/article/russia-ukraine-war-attack-sumy-trump-c798e420e87f1ef25af4f01f80128aa6"
"March 11","Apple Podcasts charts for week ending March 10","Apple Podcasts – Top New Shows","https://apnews.com/entertainment/donald-trump-donald-trump-es-joe-rogan-helen-betty-osborne-china-a0e7eba0013056f89210d726c1df641c"
"March 6","Zelenskyy and EU leaders comment ahead of emergency summit","Zelenskyy arrived at the emergency EU summit as von der Leyen proposes loosening defense budget rules.","https://apnews.com/video/zelenskyy-and-eu-leaders-comment-ahead-of-emergency-summit-73c599aded514e25b274d16b70bdc134"
"March 4","Demonstrators across 50 states look to unify a disparate opposition to Trump and his sweeping agenda","Protest groups gather nationwide to assail Trump’s presidency.","https://apnews.com/article/donald-trump-protests-53c6a993ee4892d4b5f9f90607f410e3"
"March 4","Without US help, Zelenskyy has few options except to repair his relationship with the White House","Zelenskyy faces limited options after an Oval Office row with Trump.","https://apnews.com/article/russia-ukraine-war-trump-zelenskyy-meeting-30be085063f4f6f3df242553402234f1"
"March 2","What US lawmakers are saying about the White House clash between Trump and Zelenskyy","Key Republicans and Democrats react to Trump–Zelensky confrontation.","https://apnews.com/article/republicans-trump-zelenskyy-meeting-64ec4a67fce4f04a2d189a1e0204b023"
"March 1","Trump’s Oval Office thrashing of Zelenskyy shows limits of Western allies’ ability to sway US leader","The meeting laid bare limits of allies’ ability to influence Trump.","https://apnews.com/article/trump-zelenskyy-oval-office-ukraine-russia-blowup-8aa63e55c859e8fea963911478c376ee"
"February 28","Zelenskyy leaves White House without signing minerals deal after Oval Office blowup","Trump berated Zelenskyy and canceled the planned signing.","https://apnews.com/article/zelenskyy-security-guarantees-trump-meeting-washington-eebdf97b663c2cdc9e51fa346b09591d"
"February 28","JD Vance gets his long-awaited moment to admonish Ukraine’s Zelenskyy","Vice President JD Vance was dismissing Ukraine long before the Oval Office meeting.","https://apnews.com/article/jd-vance-zelenskyy-ukraine-854b13006d0601223e5ac8d955b08a8b"
"February 28","European leaders pledge to stand by Ukraine after confrontational Oval Office meeting with Trump","European leaders express support after contentious meeting.","https://apnews.com/article/zelenskyy-europe-trump-meeting-washington-oval-office-f7a38b4f7d4d5557575e6788e27687eb"
"February 26","Trump says Zelenskyy is coming to the White House to sign US-Ukraine critical minerals deal","Trump announces a minerals agreement to be signed days later.","https://apnews.com/article/russia-ukraine-war-trump-economic-deal-faf1ff881802c923370053e539ec26e4"
"February 14","The art of the deal? Zelenskyy says a Ukraine-Russia agreement must come through Trump negotiations","Zelenskyy appeals to Trump's dealmaker image.","https://apnews.com/article/trump-zelenskyy-munich-security-conference-ukraine-1feeba7df83c4cc241370180b3673677"
"January 22","Supreme Court could revive lawsuit against Texas officer who shot motorist stopped for unpaid tolls","SCOTUS seems inclined to revive civil rights lawsuit.","https://apnews.com/article/supreme-court-police-shooting-black-motorist-texas-f8c420b609150907e843ac974b9676d4"
"November 1, 2024","Americans helping Ukraine’s war efforts say the US hasn’t done enough","Amed Khan says U.S. support is insufficient for Ukraine to win.","https://apnews.com/article/ukraine-russia-war-be08b99bf75e99de991557ac18c7bf15"
"October 20, 2024","Ukraine’s ‘victory plan’ receives mixed reactions from Western allies","Zelenskyy’s plan receives mixed feedback.","https://apnews.com/article/victory-plan-ukraine-russia-war-zelenskyy-1a66e6b1655fcaa421526ad174e618bd"
"October 18, 2024","Right-wing influencers hyped anti-Ukraine videos made by a TV producer also funded by Russian media","Ben Swann produced anti-Ukraine videos via Russian-funded company.","https://apnews.com/article/social-media-influencers-ben-swann-russia-trump-jr-ukraine-zelenskyy-9d4281756246b94eda05c478f3dac203"
"October 17, 2024","Ukraine’s former armed forces chief endorses ‘victory plan’ in first speech since his dismissal","Zaluzhnyi shows support despite tensions.","https://apnews.com/article/victory-plan-ukraine-russia-war-zelenskyy-zaluzhnyi-5634fc4a1c17a04b09a64c17b98c6512"
"October 3, 2024","New NATO chief Mark Rutte visits Ukraine in his first trip since taking office","New NATO Secretary-General Mark Rutte has visited Ukraine in his first official trip since taking office and pledging continued support for Kyiv.","https://apnews.com/article/russia-ukraine-war-kharkiv-glide-bombs-a4436a45d74456f0f199095442765957"

"September 26, 2024","Trump says he will meet with Ukrainian President Volodymyr Zelenskyy","Donald Trump announced he will meet with Ukrainian President Volodymyr Zelenskyy at a critical moment in the Russia-Ukraine war.","https://apnews.com/video/russia-ukraine-war-ukraine-government-donald-trump-volodymyr-zelenskyy-ukraine-181c9c0063be4f14a04b4efaafa38295"

"September 25, 2024","Speaker Johnson demands Zelenskyy remove Ukraine’s ambassador to US after Pennsylvania visit","House Speaker Mike Johnson is calling on Ukrainian President Volodymyr Zelenskyy to fire his country’s ambassador to the U.S.","https://apnews.com/article/zelenskyy-johnson-ambassador-ukraine-biden-harris-trump-d81b0a055d99cfd4804b3f2c00915d09"

"August 26, 2024","Russia’s deadly overnight barrage of missiles and drones hits over half of Ukraine","Russia battered much of Ukraine with scores of missiles and drones that officials say killed four people, injured more than a dozen, and damaged energy facilities.","https://apnews.com/article/russia-ukraine-war-26-august-2024-25296eee7c9c394d07d806f44a2ec09e"

"August 26, 2024","Biden speaks with Modi about Indian premier’s recent visit to Ukraine, situation in Bangladesh","President Joe Biden has spoken with Indian Prime Minister Narendra Modi following Modi’s high-profile visit to Kyiv.","https://apnews.com/article/biden-modi-russia-ukraine-bangladesh-0a9dff3ebc95bdf18633a620526c9221"

"August 7, 2024","Bob Woodward’s next book, ‘War,’ will focus on conflict abroad and politics at home","Bob Woodward's next book will focus on conflicts in Ukraine and the Middle East and their place in American politics.","https://apnews.com/article/bob-woodward-book-war-harris-trump-biden-a89ea7f31fc5aa1338e8e8361c57eee3"

"August 5, 2024","Ukraine’s medalists at the Paris Olympics face a long trek home. For some, it’s up to a 30-hour trip","Ukraine’s Olympic medalists face long and complicated journeys home amid the war.","https://apnews.com/article/ukraine-medalists-2024-olympics-paris-0e58b634e763aee579a65810d271b8b9"

"June 13, 2024","Biden and Zelenskyy sign security deal as Ukraine’s leader questions how long the unity will last","President Joe Biden and Ukrainian President Zelenskyy signed a long-term security agreement to bolster Ukraine's defenses.","https://apnews.com/article/ukraine-russia-biden-zelenskyy-assets-loan-004dba0db6b04bb5669ac30581088501"

"June 13, 2024","Biden and Zelenskyy sign security deal as Ukraine’s leader questions how long the unity will last (Video)","Biden and Zelenskyy sign a long-term security agreement aimed at strengthening Ukraine’s defenses.","https://apnews.com/video/ukraine-government-ukraine-russia-ukraine-war-italy-national-7d8fdce8a4a249789036b81dcb2066ea"

"May 7, 2024","Ukraine says it foiled a Russian spy agency plot to assassinate President Zelenskyy","Ukrainian counterintelligence investigators say they foiled a Russian plot to assassinate Zelenskyy and other top officials.","https://apnews.com/article/russia-ukraine-war-assassination-zelenskyy-4b301e9c9a1f067a45105303dff03198"

"April 29, 2024","This congresswoman was born and raised in Ukraine. She just voted against aid for her homeland","Rep. Victoria Spartz, the only Ukrainian-born U.S. lawmaker, voted against sending $61B in aid to Ukraine.","https://apnews.com/article/indiana-primary-election-victoria-spartz-ukraine-57fb403caa6a9bbe459639baacfdb7fa"

"April 23, 2024","Pentagon set to send $1 billion in new military aid to Ukraine once Biden signs bill","The Pentagon is poised to send $1B in new military aid to Ukraine after Senate passage of a major bill.","https://apnews.com/article/ukraine-russia-pentagon-weapons-congress-54045b0755b1711d0e22beaedf137cab"

"April 23, 2024","A Russian strike on Kharkiv’s TV tower is part of an intimidation campaign, Ukraine’s Zelenskyy says","Zelenskyy says the strike smashing Kharkiv’s TV tower was part of an intimidation campaign.","https://apnews.com/article/russia-ukraine-war-kharkiv-tv-tower-317bfd1aef56342a82dfa0a776dadbcc"

"April 22, 2024","Biden will send Ukraine air defense weapons, artillery once Senate approves, Zelenskyy says","Biden told Zelenskyy the U.S. will send badly needed air defense systems once legislation passes.","https://apnews.com/article/biden-ukraine-national-security-aid-russia-b172cb344d5c7867ed1370246c863794"

"April 9, 2024","China’s Xi meets with Russian Foreign Minister Lavrov in show of support against Western democracies","Xi Jinping met Russia’s Sergei Lavrov amid alignment against Western democracies.","https://apnews.com/article/china-russia-lavrov-ukraine-38cf75eb975b5fd1b9cc5b7c4dbbe33c"

"March 4, 2022","Live updates: UN council to meet on humanitarian situation","The UN Security Council will meet on the worsening humanitarian situation in Ukraine.","https://apnews.com/article/ussia-ukraine-war-live-updates-ddbace81e2e09028e0da1ec37619d148"

"February 9, 2024","Tucker Carlson was not put on a ‘kill list’ in Ukraine for Putin interview","False claims circulated that Carlson was put on a 'kill list'; AP confirms it's untrue.","https://apnews.com/article/fact-check-tucker-carlson-ukraine-kill-list-putin-376075051804"

"January 31, 2024","Rumors that Ukraine’s top commander may be dismissed expose rifts in Ukraine top brass","Reports claim Zelenskyy may fire top commander Zaluzhnyi, but were denied.","https://apnews.com/article/ukraine-zaluzhni-resigning-rumors-zelenskyy-2aec18dd5729334dc647557fb17da597"

"December 28, 2023","Biden no dijo que se necesita sacrificar hasta el último soldado ucraniano","AP Verifica: Claims that Biden said Ukrainians must fight ‘to the last soldier’ are false.","https://apnews.com/article/ap-verifica-368224510558"

"December 15, 2023","The West supports Ukraine against Russia’s aggression. So why is funding its defense in question?","Western support for Ukraine faces obstacles as political tensions rise.","https://apnews.com/article/eu-orban-zelensky-ukraine-funding-war-russia-792f315f256a10addd6647a5535aab7f"

"December 8, 2023","NOT REAL NEWS: A look at what didn’t happen this week","AP fact-checks several false claims, including ones involving Zelenskyy and Arlington.","https://apnews.com/article/fake-news-misinformation-transgender-swimmer-zelenskyy-arlington-explosion-48dda946b274d3a9240f74c8c4fa3191"

"December 4, 2023","Ukraine’s Zelenskyy did not purchase two luxury yachts in October. They’re still up for sale","False claims said Zelenskyy bought two yachts; the yachts remain unsold.","https://apnews.com/article/fact-check-zelenskyy-luxury-yachts-75-million-067680385163"

"April 25, 2022","Video of Zelenskyy talking about cocaine is deceptively edited","A 2019 interview video was mis-edited to falsely imply Zelenskyy referenced cocaine.","https://apnews.com/article/fact-checking-volodymyr-zelenskyy-drugs-137476901035"

"November 10, 2023","NOT REAL NEWS: A look at what didn’t happen this week","AP fact-checks false claims including gas leak rumors and Ukraine misinformation.","https://apnews.com/article/fact-check-misinformation-election-kentucky-pennsylvania-ukraine-e0b8109b52f85fe2cbf6e7fc56985fe4"

"November 6, 2023","No, Ukraine’s president didn’t surrender to Russia over the weekend, despite social media claims","False claims said Zelenskyy surrendered; Ukraine remains at war with Russia.","https://apnews.com/article/fact-check-ukraine-russia-war-zelenskyy-surrender-329652001741"

"October 28, 2023","Russia accuses Ukraine of damaging a nuclear waste warehouse as the battle for Avdiivika grinds on","Russia accuses Ukraine of damaging nuclear waste storage in a drone strike.","https://apnews.com/article/russia-ukraine-war-nuclear-plant-76ee3428d2aa813df6ea8f90d014529c"

"September 28, 2023","NATO’s secretary-general meets with Zelenskyy to discuss ‘ending Russia’s aggression’","NATO’s Stoltenberg met Zelenskyy to discuss war status and troop needs.","https://apnews.com/article/russia-ukraine-war-nato-ammunition-zelenskyy-stoltenberg-4f40e940d63f595445f1410dddf0ba73"

"September 22, 2023","Video of a billboard near Times Square misspelling ‘Glory to Ukraine’ was fabricated","A viral video about a Times Square billboard was fabricated.","https://apnews.com/article/fact-check-glory-to-ukraine-billboard-times-square-294989480412"

"September 17, 2023","The spotlight is on Ukraine at UN leaders’ gathering, but is there room for other global priorities?","Ukraine dominates discussions at the UN General Assembly amid global division.","https://apnews.com/article/un-general-assembly-leaders-ukraine-inequality-27e5e572b91d2598d4249c6cc029bfa0"

"September 7, 2023","King Charles III shows his reign will be more about evolution than revolution after year on the job","Charles III's reign emphasized continuity and gradual change.","https://apnews.com/article/king-charles-monarchy-queen-death-anniversary-925acede2fa2dfe3b0da3c8491feabd7"
"August 21, 2023","Greece hosts meeting of several Balkan leaders; Ukraine’s Zelenskyy also will attend","The leaders of several Balkan countries are gathering in Athens with EU officials to discuss the region’s European future.","https://apnews.com/article/balkans-european-union-greece-8745b410bdfa646ca236d0cc616a48ab"

"August 7, 2023","Video de cartel contra presidente de Ucrania en Japón fue alterado","LA AFIRMACIÓN: Un video muestra un anuncio digital en contra del presidente de Ucrania en Tokio; el video fue alterado.","https://apnews.com/ap-verifica-00000189d246db1aa7e9d3774a4a0000"

"July 15, 2023","South Korea to expand support for Ukraine as President Yoon Suk Yeol makes a surprise visit","South Korean President Yoon made a surprise visit to Ukraine after attending NATO and Poland meetings.","https://apnews.com/article/ukraine-russia-war-f374233eb81618298720c35083ac8e81"

"July 14, 2023","Fotografía de Zelenskyy en reunión de la OTAN está editada","LA AFIRMACIÓN: Fotografía manipulada afirma que Zelenskyy sostenía un trapeador en la cumbre de la OTAN.","https://apnews.com/article/ap-verifica-350730908144"

"July 5, 2023","Pence says Trump and DeSantis do not understand broader importance of US military aid to Ukraine","Mike Pence says Trump and DeSantis fail to grasp implications of limiting military aid to Ukraine.","https://apnews.com/article/pence-ukraine-china-desantis-trump-republican-4e50cd874de751661f18cbfba183f181"

"March 22, 2018","Man dead, wife injured in White Township, Indiana County","Coroner reports Daniel M. died and his wife was injured in a shooting incident.","https://apnews.com/article/archive-002aacfe15bb481f8ef05baa9ec8b26f"

"May 16, 2023","Zelenskyy’s European tour aimed to replenish Ukraine’s arsenal and build political support","European leaders promised Zelenskyy missiles, tanks and drones during a 3-day tour.","https://apnews.com/article/zelenskyy-europe-tour-weapons-jets-1cf0afe5bf3a3f5a51c5603aab2ccf5e"

"May 16, 2023","South Korea’s president vows to expand non-lethal aid to Kyiv in meeting with Ukraine’s first lady","South Korea will expand non-lethal aid after meeting Ukraine’s first lady.","https://apnews.com/article/south-korea-ukraine-yoon-zelenska-221f1b1bf0665cc2cb5b06071ee28003"

"March 29, 2023","Ukraine’s Zelenskyy: Any Russian victory could be perilous","Zelenskyy warns that Ukraine must win the prolonged battle for a key eastern city.","https://apnews.com/article/ukraine-zelenskyy-russia-putin-bakhmut-2334ec3a5b74d3cc3c4e012db71920e5"

"March 21, 2023","Publicación tergiversa declaración de embajador polaco sobre Ucrania","La afirmación de que Polonia enviaría 300,000 soldados a la guerra es falsa.","https://apnews.com/article/ap-verifica-887163984331"

"March 1, 2023","Zelenskyy no dijo que EEUU debe enviar a sus “hijos” a la guerra en Ucrania","Publicaciones tergiversan declaraciones sobre envío de tropas estadounidenses.","https://apnews.com/article/ap-verifica-479590270519"

"March 1, 2023","Zelenskyy didn’t say US troops needed to fight in Ukraine","Zelenskyy explained NATO defense obligations; he did not call for US troops in Ukraine.","https://apnews.com/article/fact-check-volodymyr-zelenskyy-ukraine-war-troops-883661209159"

"February 16, 2023","Israeli FM promises cooperation with Ukraine against Iran","Israeli FM says Ukraine and Israel will strengthen cooperation against Iran.","https://apnews.com/article/russia-ukraine-israel-f04f0a67b69a1e7fad785016fa129503"

"February 6, 2023","Wisconsin mom sent to prison for role in teen son’s death","A Wisconsin woman received 15 years for involvement in her son's fatal shooting.","https://apnews.com/article/legal-proceedings-wisconsin-crime-homicide-2edc04d0811202e33ddfce9bfea3e119"

"February 6, 2023","Zelenskyy did not ask NATO to strike Russia with nuclear weapons","False claims used altered subtitles to misrepresent Zelenskyy’s stance.","https://apnews.com/article/fact-check-zelenskyy-nato-russia-nuclear-162428316989"

"December 29, 2022","Russia hits key infrastructure with missiles across Ukraine","Russia launched major missile strikes hitting power stations and infrastructure.","https://apnews.com/article/kyiv-russia-ukraine-war-government-0a206ad866d5e19899c752d988a1a3be"

"December 22, 2022","Ukrainians hail Zelenskyy after US visit dismissed by Putin","Ukrainians praised Zelenskyy’s US visit while Russia downplayed it.","https://apnews.com/article/russia-ukraine-moscow-ce43333cf451c709a1e315a9a7b82954"

"December 22, 2022","Alaska Digest, 1pm update","Roundup of Alaska news stories.","https://apnews.com/article/covid-b8de9c9cfc6abcc29fadc095f6c5bae7"

"December 22, 2022","Michigan Digest","Roundup of Michigan news stories.","https://apnews.com/article/michigan-weather-winter-7524074c5906b0bfd3a89228ecaa05d8"

"December 22, 2022","Indiana Digest","Roundup of Indiana news stories.","https://apnews.com/article/indiana-weather-winter-80e0018f7653d25d4980ea7987889451"

"December 22, 2022","Florida News Digest","Roundup of Florida news stories.","https://apnews.com/article/tampa-bay-buccaneers-jacksonville-jaguars-florida-524316b7ad29cf791a118f55aec7865d"

"December 22, 2022","PA--Pennsylvania Digest, 130pm update","Roundup of Pennsylvania news stories.","https://apnews.com/article/nhl-pennsylvania-toronto-maple-leafs-carolina-hurricanes-pittsburgh-penguins-eda3c361f7b48bda52b2a871e28b1c36"

"December 22, 2022","OH--Ohio Digest, 130pm update","Roundup of Ohio news stories.","https://apnews.com/article/ohio-covid-30fde239342971d1aaf0d4850256906a"

"December 22, 2022","NJ--New Jersey Digest, 130pm update","Roundup of New Jersey news stories.","https://apnews.com/article/nfl-new-jersey-phil-murphy-a07f28f2d20d0fe1f43f35ad57bf4a2f"

"December 22, 2022","Maine Digest","Roundup of Maine news stories.","https://apnews.com/article/biden-covid-ac79921c08b9435c5bfe724dc9d2b354"

"December 22, 2022","Massachusetts and Rhode Island Digest","Roundup of MA & RI news stories.","https://apnews.com/article/covid-massachusetts-fc032f1c686caf568333c9f059a00c2a"

"December 22, 2022","New Hampshire Digest","Roundup of NH news stories.","https://apnews.com/article/covid-new-hampshire-baf65d1ca5c42b341813633092bb6a82"

"December 22, 2022","Vermont Digest","Roundup of Vermont news stories.","https://apnews.com/article/covid-fraud-8c37c2a19e8091c1505de7392b3d750d"

"December 22, 2022","Zelenskyy’s surprise visit to DC was months in the making","Zelenskyy’s Washington trip had been planned quietly for months.","https://apnews.com/article/putin-zelenskyy-politics-nancy-pelosi-zagreb-48d6e3aa3e13b0a9a677522260d61ba3"

"December 8, 2022","Scrutiny of Ukraine church draws praise, fear of overreach","Proposed legislation could crack down on Ukrainian Orthodox Church over ties to Moscow.","https://apnews.com/article/russia-ukraine-religion-moscow-government-1a28b354f992f6d4d7f710c691e9792e"
"December 7, 2022","Zelenskyy and ‘spirit of Ukraine’ named Time person of year","Time Magazine has named Ukrainian President Volodymyr Zelenskyy its person of the year for showing that courage can be as contagious as fear.","https://apnews.com/article/zelenskyy-kyiv-europe-63d2782889fb9ac044af6ec711433883"

"December 5, 2022","25,000 tons of Ukraine grain reach east Africa amid drought","The first shipment of grain from Ukraine’s own initiative has reached Djibouti for delivery to Ethiopia.","https://apnews.com/article/europe-africa-united-nations-kenya-djibouti-98744e73387678d791d20ecaa5237324"

"November 18, 2022","Publicaciones desinforman sobre FTX, Ucrania y el partido demócrata","Afirmación falsa: Apoyos económicos enviados a Ucrania volvieron al Partido Demócrata vía FTX.","https://apnews.com/article/ap-verifica-952943607814"

"November 17, 2022","OTAN no buscó enfrentarse a Rusia tras caída de misil en Polonia","Afirmación falsa: OTAN no planeó enfrentarse a Rusia tras la caída de misiles.","https://apnews.com/article/ap-verifica-398825319877"

"November 16, 2022","Live Updates | Russia-Ukraine-War","UN says it is cautiously optimistic a deal allowing Ukraine to export grain will be renewed.","https://apnews.com/article/russia-ukraine-nato-british-politics-europe-poland-25160d35defe45eaf6cb498ab3a11fba"

"October 27, 2022","German magazine didn’t publish cartoon cover depicting Zelenskyy","False: The magazine's editor confirmed the cartoon cover was not published.","https://apnews.com/article/fact-check-Volodymyr-Zelenskyy-magazine-335208752323"

"October 21, 2022","French ambassador to Ukraine has not resigned","False: France confirmed the ambassador remains in Ukraine.","https://apnews.com/article/fact-check-Zelenskyy-Kyiv-287770680813"

"October 14, 2022","NOT REAL NEWS: A look at what didn’t happen this week","Fact-check roundup including false claims about Zelenskyy’s office being destroyed.","https://apnews.com/article/russia-ukraine-zelenskyy-kyiv-mlb-sports-a0655af50c0ade448e470089c56e5205"

"October 13, 2022","Publicación sobre política exterior de Biden es imprecisa","Afirmación imprecisa sobre apoyo de Biden a Zelenskyy.","https://apnews.com/article/ap-verifica-225223595591"

"October 11, 2022","Russian strikes in Kyiv didn’t destroy Zelenskyy’s office","False: The office was not destroyed by missile strikes.","https://apnews.com/article/fact-check-kyiv-strikes-Zelenskyy-104100797091"

"October 6, 2022","Ukraine leader says Putin wouldn’t survive nuclear attack","Zelenskyy says Putin would not survive nuclear escalation.","https://apnews.com/article/russia-ukraine-zelenskyy-putin-moscow-nuclear-weapons-8d73ec95b94028ecfa6321250c1e01d2"

"September 27, 2022","He’s back: Italy’s Berlusconi wins Senate seat after tax ban","Berlusconi returns to Italy’s parliament after previous ban.","https://apnews.com/article/russia-ukraine-italy-silvio-berlusconi-2842b4f8c1bd726e2666e48e1f6edd54"

"September 20, 2022","Rusia no usó vía diplomática para devolver Crimea a Ucrania","Afirmación falsa: Rusia no negoció pacíficamente la devolución de Crimea.","https://apnews.com/article/ap-verifica-183592357761"

"September 2, 2022","Missing military vets’ families meet with Ukraine officials","Families of 2 missing US veterans met with Ukraine officials and US government.","https://apnews.com/article/russia-ukraine-alabama-veterans-kharkiv-94bc7030832a892de71856fbb3f311af"

"August 22, 2022","Ukraine: 9,000 of its troops killed since Russia began war","A Ukrainian general says 9,000 soldiers have been killed since the invasion began.","https://apnews.com/article/russia-ukraine-fires-eac13f4bb47663c9769696029ecc257d"

"July 18, 2022","Amid Russia shelling, Ukraine aims to strengthen government","Zelenskyy continues a major shakeup of security services, suspending 28 officials.","https://apnews.com/article/russia-ukraine-zelenskyy-kyiv-security-services-7afae942f85f76111f8130b331d7c360"

"July 3, 2022","Splintered Ukrainian city braces for new battle with Russia","Slovyansk residents prepare to defend the city again.","https://apnews.com/article/russia-ukraine-moscow-government-and-politics-a8652c890cc9583840468eafb049175e"

"June 18, 2022","Scholz: G7 will support Ukraine ‘for as long as necessary’","Germany says G7 nations will support Ukraine for as long as needed.","https://apnews.com/article/russia-ukraine-putin-politics-g-7-summit-cefbfefbb3c7ea307478391cbfa89f00"

"June 15, 2022","Time correspondent writes book on Zelenskyy and Ukraine war","A Time correspondent is writing a book with extensive access to Zelenskyy.","https://apnews.com/article/russia-ukraine-zelenskyy-entertainment-afdce68e524d97ec590c57baa2c7743c"

"June 13, 2022","Bucolic Ukraine forest is site of mass grave exhumation","Ukraine investigates killings of over 12,000 civilians.","https://apnews.com/article/russia-ukraine-kyiv-business-criminal-investigations-bed8a5fac1dab4cfcdf45aed815ff510"

"June 6, 2022","Ukraine’s leader: Russia seeks another key city in southeast","Zelenskyy says Russia aims to capture Zaporizhzhia.","https://apnews.com/article/russia-ukraine-zelenskyy-kyiv-middle-east-d1fb72e87c5571b8593f4d8e412b3725"

"May 30, 2022","Ukraine takes political path to qualifying for World Cup","Ukraine’s World Cup qualifying journey becomes political after invasion.","https://apnews.com/article/russia-ukraine-sports-soccer-scotland-a15d6288bbc4492068b8f59cbfc86a16"

"May 30, 2022","Ukraine, Russia battle in the east as Zelenskyy visits front","Russian and Ukrainian forces engage in fierce combat.","https://apnews.com/article/russia-ukraine-nato-government-and-politics-ca9849c84e6e0345a84a2cc3ea3d2383"

"May 25, 2022","Ukraine: 200 bodies found in basement in Mariupol’s ruins","Workers found 200 bodies in the basement of a destroyed building.","https://apnews.com/article/russia-ukraine-zelenskyy-kyiv-0c74a0c16b834732b81e460450da3131"

"May 23, 2022","Russian sentenced to life in Ukraine’s 1st war crimes trial","A Russian soldier receives a life sentence for killing a civilian.","https://apnews.com/article/russia-ukraine-kyiv-kharkiv-2fb1355f5c0b5724adfc5b4367807335"

"May 15, 2022","McConnell: Finland, Sweden ‘important additions’ to NATO","McConnell says Finland and Sweden would be key additions to NATO.","https://apnews.com/article/russia-ukraine-mitch-mcconnell-finland-john-cornyn-susan-collins-2e21fbc47f45788ad3448b27364bde84"

"May 14, 2022","McConnell, GOP senators meet Zelenskyy in surprise Kyiv stop","McConnell says US will support Ukraine until it wins the war.","https://apnews.com/article/mcconnell-ukraine-surprise-visit-zelenskyy-27c328d36071ad0df27be2e7f0a7970b"

"May 13, 2022","Polish citizen, not postal service, created Zelenskyy stamps","A customer created personalized Zelenskyy stamps; not official postal issue.","https://apnews.com/article/fact-check-Zelenskyy-Poland-stamps-233915515818"

"May 6, 2022","TRANSCRIPT: AP Interview with Belarusian President Alexander Lukashenko","Full English transcript of interview with Lukashenko.","https://apnews.com/article/alexander-lukashenko-interview-transcript-883228111287"

"May 4, 2022","Live updates | UN: More than 300 evacuated from Mariupol","UN says 300+ civilians evacuated from Mariupol and nearby towns.","https://apnews.com/article/russia-ukraine-covid-business-health-europe-871698afc001dab45b7d519faa2a0473"
"April 29, 2022","Publicación sobre postura de Austria ante Ucrania es engañosa","Afirmación falsa: UE está dividida; Austria no rechazó a Ucrania.","https://apnews.com/article/ap-verifica-282139389109"

"April 24, 2022","Zelenskyy video was edited to add white powder","False: The original video posted on Instagram contained no white powder.","https://apnews.com/article/fact-check-zelenskyy-desk-powder-504857917643"

"April 19, 2022","Russia pours in more troops and presses attack in the east","Russia attacks cities in Ukraine’s eastern industrial heartland.","https://apnews.com/article/russia-ukraine-putin-kyiv-world-news-europe-61ac8636ddb2d75a6df4605492889d7b"

"April 18, 2022","Live Updates | Russians fight in streets of Ukrainian town","Street battles begin in Kreminna; evacuation impossible.","https://apnews.com/article/russia-ukraine-business-europe-kharkiv-6adf2cf2568111779b9ce92d47686668"

"April 17, 2022","Live Update | Zelenskyy: Troops inflict ‘deliberate terror’","Zelenskyy says Russian troops carry out torture and kidnappings in the south.","https://apnews.com/article/russia-ukraine-business-bulgaria-europe-humanitarian-assistance-d0c9d752295a93aafa0527b8049feee9"

"April 11, 2022","Zelenskyy asks South Korea to provide arms to fight Russia","Zelenskyy urges South Korea to supply weapons to Ukraine.","https://apnews.com/article/russia-ukraine-zelenskyy-europe-south-korea-seoul-6320ab452a94b976d1a19e7ef8b4af3c"

"April 7, 2022","No truth to claims Zelenskyy, Soros are cousins","False: Zelenskyy and Soros are not related.","https://apnews.com/article/fact-checking-586448883875"

"April 2, 2022","Several colleges eye honorary degrees for Ukraine’s Zelensky","At least 17 colleges plan honorary degrees for Zelensky.","https://apnews.com/article/russia-ukraine-zelenskyy-new-york-education-lifestyle-7284a31de365248a9d185356bfbb1145"

"April 2, 2022","Live updates | Zelenskyy won’t discuss fuel depot attack","Zelenskyy declines to comment on alleged order to strike fuel depot.","https://apnews.com/article/russia-ukraine-business-europe-japan-poland-8b1d6dc3150020709de3bb07f798d716"

"March 24, 2022","Russia-Ukraine war: Key things to know about the conflict","Zelenskyy urges Ukrainians to keep resisting Russia’s invading forces.","https://apnews.com/article/russia-ukraine-putin-kyiv-nato-g-7-summit-a25f50750c18ccdaa2ef9b8184142e2b"

"March 21, 2022","Video no muestra a presidente de Ucrania y esposa cantando","Falso: el video de Zelenskyy y Zelenska cantando es un montaje.","https://apnews.com/article/ap-verifica-016665126811"

"March 18, 2022","Zelenskyy’s shirt featured Ukraine military emblem, not hate symbol","False: Shirt showed Ukraine Armed Forces emblem, not extremist symbol.","https://apnews.com/article/fact-checking-497022700383"

"March 16, 2022","Russia’s onslaught continues amid optimism over talks","Airstrike destroyed Mariupol theater where civilians sheltered.","https://apnews.com/article/russia-ukraine-zelenskyy-kyiv-europe-congress-058c8b72b81044f861b30b7ceb500a15"

"March 16, 2022","Video no muestra un ataque en París, es un montaje","Falso: video no representa un ataque reciente en París.","https://apnews.com/article/ap-verifica-584299607986"

"March 14, 2022","Zelenskyy to deliver virtual address to US Congress","Zelenskyy will address both House and Senate virtually.","https://apnews.com/article/russia-ukrriane-volodymyr-zelensky-congress-address-babf66809eec5138482d14cee7f32221"

"March 8, 2022","Retired professor mounts GOP challenge to Democrat DeLauro","Lesley DeNardis announces run against Rep. Rosa DeLauro.","https://apnews.com/article/2022-midterm-elections-elections-connecticut-new-haven-congress-372a35015c1c886ad003322d75b36465"

"March 6, 2022","Western Wyoming Ukrainians, friends, demonstrate support","Supporters gather in Jackson to back Ukraine.","https://apnews.com/general-news-57cc38334dedb894ba3eaa60280acb63"

"March 5, 2022","Live updates: Ukrainian paramedic remembered for bravery","China tells US not to “add fuel to the flames” in Ukraine.","https://apnews.com/article/russia-ukraine-business-united-nations-europe-singapore-42fc449b3e3336d09660c273aa0d9f19"

"March 4, 2022","Russian propaganda ‘outgunned’ by social media rebuttals","Russia spreads false claims Zelenskyy fled Kyiv.","https://apnews.com/article/russia-ukraine-volodymyr-zelenskyy-kyiv-technology-misinformation-5e884b85f8dbb54d16f5f10d105fe850"

"March 1, 2022","Fotos de presidente de Ucrania y mujeres soldado no son recientes","Falso: fotos no corresponden a la guerra de 2022.","https://apnews.com/article/ap-verifica-964416835604"

"February 24, 2022","Live updates: Ukraine diplomat urges China to talk to Putin","Ukraine urges China to help stop Russian “massacre.”","https://apnews.com/article/russia-ukraine-latest-updates-0224-303b0bfdc6148c8738d6ac0ca78142fd"

"February 24, 2022","Russia attacks Ukraine as defiant Putin warns US, NATO","Russia launches full-scale invasion; Putin threatens consequences.","https://apnews.com/article/russia-ukraine-europe-russia-moscow-kyiv-626a8c5ec22217bacb24ece60fac4fe1"

"January 24, 2022","Analysis: Crisis in Ukraine a showdown of two world views","Analysis of Ukraine crisis and geopolitical stakes.","https://apnews.com/article/russia-ukraine-russia-vladimir-putin-soviet-union-europe-32b8a914ad4debba6c3231738a5f5a36"

"September 22, 2019","Lindsey Graham calls for Biden-Ukraine Justice Department probe","Graham urges DOJ to investigate alleged Biden–Ukraine link.","https://apnews.com/article/joe-biden-business-europe-ukraine-lindsey-graham-4244c50f9882fa12d0ec076cf87ffb60"

"September 30, 2021","Takeaways from Trump aide’s account of chaotic White House","Trump aide describes chaotic White House and troubling behavior.","https://apnews.com/article/donald-trump-entertainment-europe-arts-and-entertainment-royalty-25b7dbdaaafd46a5e95df14c7d2f3b39"

"October 1, 2019","Volodymyr Zelensky, Ukraine’s president, says he’s had no contact with Rudy Giuliani","Zelenskyy denies meeting or speaking with Rudy Giuliani.","https://apnews.com/article/europe-ukraine-dbdd906f0b04b9a70b9ad6402ab4f003"

"October 2, 2019","Congressman Gosar chats with Havasu, Mohave County leaders while receiving chamber award","Gosar warns of political instability during chamber event.","https://apnews.com/article/business-tax-reform-paul-gosar-439b31456ae648f0bec6a9dc89d7a05e"

"October 1, 2019","Heinrich, in Santa Fe, slams president amid impeachment inquiry","Sen. Heinrich criticizes Trump during Santa Fe visit.","https://apnews.com/article/joe-biden-donald-trump-united-states-new-mexico-impeachments-592934f106c04f358b9cfb9120366c7c"

"August 24, 2021","Fotografía que muestra evento religioso en Ucrania no es reciente","Foto viral no corresponde a evento actual en Kiev.","https://apnews.com/article/ap-verifica-309181885813"

"December 5, 2019","Vladimir Putin uses impeachment to exacerbate rifts in U.S.","Putin exploits US political division over impeachment.","https://apnews.com/article/joe-biden-europe-business-vladimir-putin-impeachments-6f194bbe8b0dc782fbd1e5c7feb498c1"

"""
from io import StringIO
df = pd.read_csv(StringIO(csv_text))
df.to_csv("zelenskyy_foxnews.csv", index=False)
