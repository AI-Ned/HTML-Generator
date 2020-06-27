## code structure ##

# User select template from GUI
# opens html template file
# template = read.html=template
# Header  input location, split template -- {Header Keyword} --  split html  = Header_html
# Article input location, Split template -- {article Keyword} -- split html  = Article_html
# Image url location, split template -- {image keyword} -- split html = image_html
# remove {Header keyword}, {article keyword}, {image Keyword}
# get user input for header, article, new image url
# rebuild the html -- header_html + header + article_html + article + image_html + image + remaining html
# create new file, write html to file, save file as .html


