
from datetime import datetime as dt

####################################################################################################

VIDEO_PREFIX = "/video/skygo"

NAME = L('Title')

ART = 'art-default.jpg'
ICON = 'icon-default.png'
ICON_SEARCH = 'icon-search.png'

BASE_URL = 'http://go.sky.com'
PLAYER_URL = 'http://go.sky.com/vod/page/tvListing.do?epgChannelId=%s'
CHANNEL_LOGO_URL = 'http://epgstatic.sky.com/epgdata/1.0/newchanlogos/200/200/skychb%s.png'
EPG_URL = 'http://www.sky.com/tvlistings-proxy/TVListingsProxy/tvlistings.json?detail=2&dur=1440&time=%(time)s&channels=%(channels)s'
ON_DEMAND_URL = 'http://go.sky.com/vod/content/%s/Browse_by_Genre/%s/content/default/promoPage.do'
SEARCH_URL = 'http://go.sky.com/vod/content/Home/Application_Navigation/Search_All/content/default/search.do?searchTerm=%s&searchTypeFilter=titleNameSearch'

# Entertainment
SKY_ONE = "1402"
SKY_LIVING = "2201"
SKY_ATLANTIC = "1412"
GOLD = "2304"
SKY_LIVING_IT = "2207"
MTV = "2501"

# Lifestyle
SKY_ARTS_ONE = "1752"

# Movies
SKY_PREMIERE = "1409"
SKY_SHOWCASE = "1814"
SKY_ACTION = "1001"
SKY_FAMILY = "1808"

# Sports
SKY_SPORTS_ONE = "1301"
SKY_SPORTS_TWO = "1302"
SKY_SPORTS_THREE = "1333"
SKY_SPORTS_FOUR = "1322"
SKY_SPORTS_NEWS = "1314"
EURO_SPORT = "1726"
EURO_SPORT_TWO = "1841"
ESPN = "3141"
ESPN_CLASSIC = "3221"
SKY_SPORTS_XTRA = "499"

# Children
CARTOON_NETWORK = "5601"
BOOMERANG = "5609"
NICKELODEON = "1846"
NICKELODEON_JR = "1857"
DISNEY_XD = "1843"
DISNEY_CHANNEL = "1881"

# Documentaries
NAT_GEO = "1806"
NAT_GEO_WILD = "1847"
HISTORY = "1875"
EDEN = "2302"
CRIME_AND_INVESTIGATION = "1448"

# News
SKY_NEWS = "1404"

####################################################################################################

channels = { 
    "106": { 
        'url': SKY_ONE, 
        'title': L('Sky1Title'), 
        'subtitle': L('Sky1Subtitle'), 
        'summary': L('Sky1Summary')},
    "107": {
        'url': SKY_LIVING, 
        'title': L('SkyLivingTitle'), 
        'subtitle': L('SkyLivingSubtitle'), 
        'summary': L('SkyLivingSummary')},
    "108": {
        'url': SKY_ATLANTIC, 
        'title': L('SkyAtlanticTitle'), 
        'subtitle': L('SkyAtlanticSubtitle'), 
        'summary': L('SkyAtlanticSummary')},
    "110": {
        'url': GOLD, 
        'title': L('GoldTitle'), 
        'subtitle': L('GoldSubtitle'), 
        'summary': L('GoldSummary')},
    "122": {
        'url': SKY_LIVING_IT, 
        'title': L('SkyLivingitTitle'), 
        'subtitle': L('SkyLivingitSubtitle'), 
        'summary': L('SkyLivingitSummary')},
    "126": {
        'url': MTV, 
        'title': L('MTVTitle'), 
        'subtitle': L('MTVSubtitle'), 
        'summary': L('MTVSummary')},
    "243": {
        'url': SKY_ARTS_ONE, 
        'title': L('SkyArts1Title'), 
        'subtitle': L('SkyArts1Subtitle'), 
        'summary': L('SkyArts1Summary')},
    "301": {
        'url': SKY_PREMIERE, 
        'title': L('SkyPremiereTitle'), 
        'subtitle': L('SkyPremiereSubtitle'), 
        'summary': L('SkyPremiereSummary')},
    "303": {
        'url': SKY_SHOWCASE, 
        'title': L('SkyMoviesShowcaseTitle'), 
        'subtitle': L('SkyMoviesShowcaseSubtitle'), 
        'summary': L('SkyMoviesShowcaseSummary')},
    "305": {
        'url': SKY_ACTION, 
        'title': L('SkyMoviesActionAdventureTitle'), 
        'subtitle': L('SkyMoviesActionAdventureSubtitle'), 
        'summary': L('SkyMoviesActionAdventureSummary')},
    "306": {
        'url': SKY_FAMILY, 
        'title': L('SkyMoviesFamilyTitle'), 
        'subtitle': L('SkyMoviesFamilySubtitle'), 
        'summary': L('SkyMoviesFamilySummary')},
    "401": {
        'url': SKY_SPORTS_ONE, 
        'title': L('SkySports1Title'), 
        'subtitle': L('SkySports1Subtitle'), 
        'summary': L('SkySports1Summary')},
    "402": {
        'url': SKY_SPORTS_TWO, 
        'title': L('SkySports2Title'), 
        'subtitle': L('SkySports2Subtitle'), 
        'summary': L('SkySports2Summary')},
    "403": {
        'url': SKY_SPORTS_THREE, 
        'title': L('SkySports3Title'), 
        'subtitle': L('SkySports3Subtitle'), 
        'summary': L('SkySports3Summary')},
    "404": {
        'url': SKY_SPORTS_FOUR, 
        'title': L('SkySports4Title'), 
        'subtitle': L('SkySports4Subtitle'), 
        'summary': L('SkySports4Summary')},
    "405": {
        'url': SKY_SPORTS_NEWS, 
        'title': L('SkySportsNewsTitle'), 
        'subtitle': L('SkySportsNewsSubtitle'), 
        'summary': L('SkySportsNewsSummary')},
    "410": {
        'url': EURO_SPORT, 
        'title': L('EurosportTitle'), 
        'subtitle': L('EurosportSubtitle'), 
        'summary': L('EurosportSummary')},
    "411": {
        'url': EURO_SPORT_TWO, 
        'title': L('Eurosport2Title'), 
        'subtitle': L('Eurosport2Subtitle'), 
        'summary': L('Eurosport2Summary')},
    "417": {
        'url': ESPN,
        'title': L('ESPNTitle'), 
        'subtitle': L('ESPNSubtitle'), 
        'summary': L('ESPNSummary')},
    "442": {
        'url': ESPN_CLASSIC,
        'title': L('ESPNClassicTitle'), 
        'subtitle': L('ESPNClassicSubtitle'), 
        'summary': L('ESPNClassicSummary')},
    "499": {
        'url': SKY_SPORTS_XTRA, 
        'title': L('SkySportsXtraTitle'), 
        'subtitle': L('SkySportsXtraSubtitle'), 
        'summary': L('SkySportsXtraSummary')},
    "501": {
        'url': SKY_NEWS, 
        'title': L('SkyNewsTitle'), 
        'subtitle': L('SkyNewsSubtitle'), 
        'summary': L('SkyNewsSummary')},
    "526": {
        'url': NAT_GEO, 
        'title': L('NatGeoTitle'), 
        'subtitle': L('NatGeoSubtitle'), 
        'summary': L('NatGeoSummary')},
    "528": {
        'url': NAT_GEO_WILD, 
        'title': L('NatGeoWildTitle'), 
        'subtitle': L('NatGeoWildSubtitle'), 
        'summary': L('NatGeoWildSummary')},
    "529": {
        'url': HISTORY, 
        'title': L('HistoryTitle'), 
        'subtitle': L('HistorySubtitle'), 
        'summary': L('HistorySummary')},
    "532": {
        'url': EDEN, 
        'title': L('EdenTitle'), 
        'subtitle': L('EdenSubtitle'), 
        'summary': L('EdenSummary')},
    "553": {
        'url': CRIME_AND_INVESTIGATION, 
        'title': L('CrimeInvestigationTitle'), 
        'subtitle': L('CrimeInvestigationSubtitle'), 
        'summary': L('CrimeInvestigationSummary')},
    "601": {
        'url': CARTOON_NETWORK, 
        'title': L('CartoonNetworkTitle'), 
        'subtitle': L('CartoonNetworkSubtitle'), 
        'summary': L('CartoonNetworkSummary')},
    "603": {
        'url': BOOMERANG, 
        'title': L('BoomerangTitle'), 
        'subtitle': L('BoomerangSubtitle'), 
        'summary': L('BoomerangSummary')},
    "604": {
        'url': NICKELODEON, 
        'title': L('NickelodeonTitle'), 
        'subtitle': L('NickelodeonSubtitle'), 
        'summary': L('NickelodeonSummary')},
    "607": {
        'url': DISNEY_XD, 
        'title': L('DisneyXDTitle'), 
        'subtitle': L('DisneyXDSubtitle'), 
        'summary': L('DisneyXDSummary')},
    "609": {
        'url': DISNEY_CHANNEL, 
        'title': L('DisneyChannelTitle'), 
        'subtitle': L('DisneyChannelSubtitle'), 
        'summary': L('DisneyChannelSummary')},
    "615": {
        'url': NICKELODEON_JR, 
        'title': L('NickelodeonJrTitle'), 
        'subtitle': L('NickelodeonJrSubtitle'), 
        'summary': L('NickelodeonJrSummary')}}

group_names = [ 
    str(L('Entertainment')), 
    str(L('Lifestyle')), 
    str(L('Movies')), 
    str(L('Sports')), 
    str(L('News')), 
    str(L('Documentaries')), 
    str(L('Kids'))]

groups = {
    str(L('Entertainment')): [ "106", "107", "108", "110", "122", "126" ],
    str(L('Lifestyle')): [ "243" ],
    str(L('Movies')): [ "301", "303", "305", "306" ],
    str(L('Sports')): [ "401", "402", "403", "404", "405", "410", "411", "417", "442", "499" ],
    str(L('News')): [ "501" ],
    str(L('Documentaries')): [ "526", "528", "529", "532", "553" ],
    str(L('Kids')): [ "601", "603", "604", "607", "609", "615" ]}

on_demand_channels = {
    str(L('Entertainment')): {
        'name': "SKYENTERTAINMENT",
        'categories': [ "Drama", "Action", "Sci Fi", "Comedy", "Reality", "Game Shows" ]},
    str(L('Lifestyle')): {
        'name': "SKYCULTURE",
        'categories': [ "Arts and Culture", "Film and Literature", "Homes", "Music", "Performance" ]},
    str(L('Movies')): {
        'name': "SKYMOVIES",
        'categories': [ "Showcase", "Comedy", "Action", "Family", "Crime and Thriller", "Sci-Fi", "Drama", "Horror", "Modern Greats", "Classics", "Indie"]},
    str(L('Sports')): {
        'name': "SKYSPORTS",
        'categories': [ "Football", "Rugby Union", "Cricket", "Golf", "Boxing", "Motorsports", "Darts", "Features", "Tennis"]},
    str(L('News')): {
        'name': "SKYNEWS",
        'categories': [ "Current Affairs", "Factual"]},
    str(L('Documentaries')): {
        'name': "SKYDOCUMENTARIES",
        'categories': [ "Crime", "Engineering", "History", "Science and Nature", "Society and Civilisation"]},
    str(L('Kids')): {
        'name': "SKYKIDS",
        'categories': [ "Activities", "Animation", "Adventure", "Entertainment and Comedy", "Educational", "Music", "Teen"]}
}

####################################################################################################

# This function is initially called by the PMS framework to initialize the plugin. This includes
# setting up the Plugin static instance along with the displayed artwork.
def Start():

    # Initialize the plugin
    Plugin.AddPrefixHandler(VIDEO_PREFIX, MainMenu, NAME, ICON, ART)
    Plugin.AddViewGroup("List", viewMode = "List", mediaType = "items")
    Plugin.AddViewGroup("InfoList", viewMode = "InfoList", mediaType = "items")

    # Setup the artwork associated with the plugin
    MediaContainer.art = R(ART)
    MediaContainer.title1 = NAME
    MediaContainer.viewGroup = "InfoList"
    DirectoryItem.thumb = R(ICON)

    HTTP.Headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-us) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27'

# This main function will setup the displayed items. This will depend if the user is currently 
# logged in.
def MainMenu():
    dir = MediaContainer(viewMode="List")
    
    dir.Append(Function(DirectoryItem(LiveMenu, "Channels")))
    dir.Append(Function(DirectoryItem(OnDemandMainMenu, "Anytime+")))
    dir.Append(Function(InputDirectoryItem(Search, L('Search'), L('SearchPrompt'), thumb = R(ICON_SEARCH))))
    
    # Preferences
    dir.Append(PrefsItem(L('Preferences'), thumb=R('icon-prefs.png')))
    
    return dir

####################################################################################################

# This function will display the available live channels
def LiveMenu(sender):
    dir = MediaContainer(disabledViewModes=["Coverflow"], title1 = L('Title'))

    # List all the different group names
    for group_name in group_names:
    
        dir.Append(Function(
            DirectoryItem(
                GroupMenu,
                group_name),
                group_name = group_name))

    return dir

# This function will display a specific group.
def GroupMenu(sender, group_name = ''):
    dir = MediaContainer(title2 = group_name)

    # Create a new item for every channel
    for channel_number in groups[group_name]:
        
        channel = channels[channel_number]
        
        # Attempt to determine the title and description of the show playing now and next. If
        # nothing is returned, then we should just assume failure and simply use the channel's
        # own information.
        now_and_next = NowAndNext(channel['url'])
        description = channel['summary']
        if now_and_next != "":
            description = "%s\n\nNow: %s\n%s\n\nNext: %s\n%s"
            description = description % (
                channel['summary'], 
                now_and_next['Now']['Title'], 
                now_and_next['Now']['Description'], 
                now_and_next['Next']['Title'], 
                now_and_next['Next']['Description'])
        
        dir.Append(WebVideoItem(
            GenerateFullUrl(channel['url']),
            title = channel['title'],
            subtitle = channel['subtitle'],
            summary = description,
            infoLabel = channel_number,
            thumb = CHANNEL_LOGO_URL % channel['url']))
    
    return dir

# This function will return details of what is currently playing, and what is next, for the given 
# channel. This information includes the name of the show, along with a brief description.
def NowAndNext(channel_url):
    epg = JSON.ObjectFromURL(EPG_URL % dict(time = dt.now().strftime('%Y%m%d%H%M'), channels = channel_url))

    # Check to see if we've received anything.
    if epg == "":
        return ""
    
    # Check to see if we have been given any channel.
    if epg.has_key('channels') == False:
        return ""
    
    channel_collection = epg['channels']

    # Check to see if we have been given any programs.
    if channel_collection.has_key('program') == False:
        return ""

    programs = channel_collection['program']

    # Ensure that we have at least two programs in order to display now and next.
    if len(programs) < 2:
        return ""

    # Determine the details of the titles which are "Now and Next"
    now_title = programs[0]['title']
    now_desc = ""
    if programs[0].has_key('shortDesc'):
        now_desc = programs[0]['shortDesc']

    next_title = programs[1]['title']
    next_desc = ""
    if programs[1].has_key('shortDesc'):
        next_desc = programs[1]['shortDesc']
    
    return { "Now" : { "Title": now_title, "Description": now_desc }, "Next" : { "Title": next_title, "Description": next_desc } }

# This function will generate a suitable URL for the required channel, using the appropriate quality
# setting currently selected by the user in their preferences.
def GenerateFullUrl(channelUrl):
    if Prefs['quality'] == "Auto":
        return (PLAYER_URL % channelUrl) + "&quality=4"
    elif Prefs['quality'] == "High":
        return (PLAYER_URL % channelUrl) + "&quality=3"
    elif Prefs['quality'] == "Medium":
        return (PLAYER_URL % channelUrl) + "&quality=2"
    else:
        return (PLAYER_URL % channelUrl) + "&quality=1"

####################################################################################################

# This function displays the first OnDemand menu. It contains a list of all the available channels.
def OnDemandMainMenu(sender):
    dir = MediaContainer(disabledViewModes=["Coverflow"], title1 = L('Title'))

    # List all the different group names
    for group_name in group_names:
        dir.Append(Function(
            DirectoryItem(
                OnDemandChannelMenu,
                group_name),
                channel_name = group_name))
    
    return dir

# This function displays the available genres which can be played on demand.
def OnDemandChannelMenu(sender, channel_name = ""):
    dir = MediaContainer(disabledViewModes=["Coverflow"], title1 = L('Title'))

    channel_details = on_demand_channels[channel_name]
    for category in channel_details['categories']:
        dir.Append(Function(
            DirectoryItem(
                OnDemandCategoryMenu,
                category),
                channel_name = channel_name,
                category_name = category))

    return dir

# This function displays the titles available for the selected genre. If the found URL contains
# a reference to a series identifier, it will present the option to select an individual episode.
def OnDemandCategoryMenu(sender, channel_name = "", category_name = ""):
    dir = MediaContainer(disabledViewModes=["Coverflow"], title1 = L('Title'))

    on_demand_channels[channel_name]['name']
    for title_detail in TitleDetails(ON_DEMAND_URL % (on_demand_channels[channel_name]['name'], category_name.replace(' ', '_'))):
        
        url = title_detail['url']
        
        # We should only display content which actually comes from the skygo website. It's 
        # possible that some titles might actually be linked to the BBC
        if url.startswith("http://go.sky.com/vod") == False:
            continue
        
        # If the associated URL is pointing to a series, then we need to transition into a sub-menu
        if url.find('/seriesId/') != -1:
            dir.Append(Function(
                DirectoryItem(
                    OnDemandSeriesMenu,
                    title_detail['title'],
                    subtitle = title_detail['subtitle'],
                    summary = title_detail['summary'],
                    infoLabel = title_detail['label'],
                    thumb = title_detail['image']),
                    series_url = url))
        else:
            dir.Append(WebVideoItem(
                url,
                title = title_detail['title'],
                subtitle = title_detail['subtitle'],
                summary = title_detail['summary'],
                infoLabel = title_detail['label'],
                thumb = title_detail['image']))

    return dir
             
# This function displays the known episode for the selected series.
def OnDemandSeriesMenu(sender, series_url):                       
    dir = MediaContainer(disabledViewModes=["Coverflow"], title1 = L('Title'))   
    
    for title_detail in TitleDetails(series_url):
        
        url = title_detail['url']
        
        # We should only display content which actually comes from the go website. It's 
        # possible that some titles might actually be linked to the BBC
        if url.startswith("http://go.sky.com/vod") == False:
            continue
        
        dir.Append(WebVideoItem(
            url,
            title = title_detail['title'],
            subtitle = title_detail['subtitle'],
            summary = title_detail['summary'],
            infoLabel = title_detail['label'],
            thumb = title_detail['image']))
    
    # If there are no titles, we should warn the user.
    if len(dir) == 0:
        return MessageContainer(sender.itemTitle, L('ErrorNoTitles'))
    
    return dir

def TitleDetails(url):
    page = HTML.ElementFromURL(url)

    titles = []
    
    # Slots
    # These elements are normally located at the top of the page and contain the featured titles
    # available for the current category. 
    slots = page.xpath("//li[contains(concat(' ',normalize-space(@class),' '),' smallSlot ')]")
    for slot in slots:
        title = slot.xpath(".//h3/span/text()")[0]
        description = slot.xpath(".//div[@class='slotDetails']/div[@class='synopsis']/p/text()")[0]

        image = ""
        image_style = slot.xpath(".//div[@class='slotBkg']")[0].get('style')
        image_style_split = image_style.split("'")
        if len(image_style_split) == 3:
            image = image_style_split[1]
 
        # If the specified URL is relative, then translate it
        if image.startswith("http") == False:
            image = BASE_URL + String.Quote(image)
        
        # If the specified URL is relative, then translate it
        url = slot.xpath(".//a[contains(concat(' ',normalize-space(@class),' '),' slideButton ')]")[0].get('href')
        if url.startswith("http") == False:
            url = BASE_URL + url
    
        titles.append({
            'title': title, 
            'summary': description,
            'subtitle': "",
            'label': "Feature",
            'image': image,
            'url': url})
    
    # Video Components
    # These elements tend to be used when displaying movies. They contain a description field which
    # is useful as a summary.
    video_components = page.xpath("//div[contains(@class, 'video-component')]")
    for component in video_components:
        title = component.xpath(".//h3/a/text()")[0].lstrip().rstrip()
        description = component.xpath(".//p/text()")[0]
 
        # If the specified URL is relative, then translate it
        image = component.xpath(".//img")[0].get('src')
        if image.startswith("http") == False:
            image = BASE_URL + String.Quote(image)
        
        # If the specified URL is relative, then translate it
        url = component.xpath(".//a")[0].get('href')
        if url.startswith("http") == False:
            url = BASE_URL + url
    
        titles.append({
            'title': title, 
            'summary': description,
            'subtitle': "",
            'label': "",
            'image': image,
            'url': url})
    
    # Promo Items
    # These are used most commonly when displayed list of series and episodes.
    items = page.xpath("//div[@class='listRows ']/div[contains(concat(' ',normalize-space(@class),' '),' promoItem ')]")
    for item in items:
        
        title = item.xpath(".//h3")[0].get('title')

        # If the specified URL is relative, then translate it
        image = item.xpath(".//img")[0].get('src')
        if image.startswith("http") == False:
            image = BASE_URL + String.Quote(image)
        
        # If the specified URL is relative, then translate it
        url = item.xpath(".//a")[0].get('href')
        if url.startswith("http") == False:
            url = BASE_URL + url
        
        channel = ""
        try:
            channel = item.xpath(".//span[@class='broadcastChannel']/text()")[0]
        except:
            pass

        titles.append({
            'title': title, 
            'summary': "",
            'subtitle': channel,
            'label': "",
            'image': image,
            'url': url})

    return titles

####################################################################################################

def Search(sender, query, url = None):
    dir = MediaContainer(viewGroup = 'InfoList', title2 = sender.itemTitle)
    
    url = SEARCH_URL % String.Quote(query)
    search_page = HTML.ElementFromURL(url)

    items = search_page.xpath("//div[@class='resultsBlock']//div[@class='promoItem ']")
    for item in items:
    
        title = item.xpath(".//div[@class='synopsisText']/h2/a/text()")[0]
    
        # If the specified URL is relative, then translate it
        image = item.xpath("./a//img")[0].get('src')
        if image.startswith("http") == False:
            image = BASE_URL + image
    
        # If the specified URL is relative, then translate it
        url = item.xpath(".//a")[0].get('href')
        if url.startswith("http") == False:
            url = BASE_URL + url
    
        # [Optional] - The Summary
        summary = None
        try: summary = item.xpath(".//div[@class='synopsisText']/p/text()")[0]
        except: pass
                
        # [Optional] - The Summary
        subtitle = None
        try: subtitle = item.xpath(".//div[@class='synopsisText']//div[@class='availability']/text()")[0]
        except: pass
    
        # Add the found item to the collection
        dir.Append(WebVideoItem(
            url,
            title = title,
            subtitle = subtitle,
            summary = summary,
            thumb = image))

    # If there are no titles, we should warn the user.
    if len(dir) == 0:
        return MessageContainer(sender.itemTitle, L('ErrorNoTitles'))
            
    return dir