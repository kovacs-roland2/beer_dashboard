import xlsxwriter

with open('/Users/roland/Downloads/recipes_full.txt', encoding="utf-8") as f:
    recipes = list(f)

#exclude ratings
current = 0
for recipe in recipes:

    for i in range(len(recipe)):

        if recipe[i:i+9] == '"rating":':
            begin_rating = i

        if recipe[i:i+8] == '"views":':
            end_rating = i
    
    recipes[current] = recipe.replace(recipe[begin_rating:end_rating],'')
    current += 1
    print('Exclude ratings: ' + str(round((current)/len(recipes)* 100,2)) + '%')


#arrays for the tables
recipes_array = []
fermentables_array = []
hops_array = []
others_array = []
yeast_array = []



#recipe_array - main table
current_recipes_array = 0
for recipe in recipes:

    for i in range(len(recipe)):

        if recipe[i:i+7] == '"name":':
            start_name = i
            end_name = i + 7

        if recipe[i:i+6] == '"url":':
            start_url = i
            end_url = i + 6

        if recipe[i:i+9] == '"method":':
            start_method = i
            end_method = i + 9

        if recipe[i:i+8] == '"style":':
            start_style = i
            end_style = i + 8

        if recipe[i:i+8] == '"batch":':
            start_batch = i
            end_batch = i + 8
        
        if recipe[i:i+5] == '"og":':
            start_og = i
            end_og = i + 5

        if recipe[i:i+5] == '"fg":':
            start_fg = i
            end_fg = i + 5

        if recipe[i:i+6] == '"abv":':
            start_abv = i
            end_abv = i + 6

        if recipe[i:i+6] == '"ibu":':
            start_ibu = i
            end_ibu = i + 6

        if recipe[i:i+8] == '"color":':
            start_color = i
            end_color = i + 8

        if recipe[i:i+10] == '"ph mash":':
            start_ph = i
            end_ph = i + 10

        if recipe[i:i+8] == '"views":':
            start_views = i
            end_views = i + 8 
        
        if recipe[i:i+15] == '"fermentables":':
            start_fermentables = i
            end_fermentables = i + 15 

    recipe_id = current_recipes_array
    name = recipe[end_name + 2 : start_url - 3]
    url = recipe[end_url + 2 : start_method - 3]
    method = recipe[end_method + 2 : start_style - 3]
    style = recipe[end_style + 2 : start_batch - 3]
    batch = recipe[end_batch + 1 : start_og - 2].replace('.',',')
    og = recipe[end_og + 1 : start_fg - 2].replace('.',',')
    fg = recipe[end_fg + 1 : start_abv - 2].replace('.',',')
    abv = recipe[end_abv + 1 : start_ibu - 2].replace('.',',')
    ibu = recipe[end_ibu + 1 : start_color - 2].replace('.',',')
    color = recipe[end_color + 1 : start_ph - 2].replace('.',',')
    ph = recipe[end_ph + 1 : start_fermentables - 2].replace('.',',')
    views = recipe[end_views + 1 : -3]      

    record = str(recipe_id) + ';' + str(url) + ';' + str(name) + ';' + str(method) + ';' + str(style) + ';' + str(batch) + ';' + str(og) + ';' + str(fg)  + ';' + str(abv) + ';' + str(ibu) + ';' + str(color) + ';' + str(ph) + ';' + str(views)
    recipes_array.append(record)

    current_recipes_array += 1
    print('Creating main table: ' + str(round((current_recipes_array)/len(recipes)* 100,2)) + '%')

#print('/n')
#print(recipes_array)



################Creating fermentable table
#fermentables_array
current_fermentables_array = 0
for recipe in recipes:

    for i in range(len(recipe)):

        if recipe[i:i+15] == '"fermentables":':
            start_fermentables = i
            end_fermentables = i + 15 

        if recipe[i:i+7] == '"hops":':
            start_hops = i
            end_hops = i + 7

    recipe_id = current_fermentables_array
    fermentables = recipe[end_fermentables + 2 : start_hops - 2]

    record = str(recipe_id) + ';' + str(fermentables)
    fermentables_array.append(record)

    current_fermentables_array += 1

    print('Creating fermentables array: ' + str(round((current_fermentables_array+1)/len(recipes)* 100,2)) + '%')
    print(recipe_id)

#print('/n')
#print(fermentables_array)


#fermentables table
fermentables_table = []
for f in fermentables_array:
    recipe_id = f[:str(f).find(';')]
    start_par = []
    end_par = []

    for i in range(len(f)):
        if f[i] == '[':
            start_par.append(i)
        if f[i] == ']':
            end_par.append(i)

    for x in range(len(start_par)):
        #changing the , char to '' in the name
        fermentables = str(f[start_par[x]+1:end_par[x]])
        char_array = []
        for ff in range(len(fermentables)):
            if fermentables[ff] == '"':
                char_array.append(ff)
        try:
            fermentables = fermentables[:char_array[0] - 1] + fermentables[char_array[0]:char_array[1]].replace(',','') + fermentables[char_array[1] + 1:]
        except:
            fermentables = str(f[start_par[x]+1:end_par[x]])


        record = str(recipe_id) + ';' + str(fermentables).replace(',',';').replace('"','').replace('.',',')
        fermentables_table.append(record)
    
    print('Creating fermentables table: ' + str(round((int(f[0])+1)/len(fermentables_array)* 100,2)) + '%')

#print('/n')
#print(fermentables_table)




##################Creating hops table
#hops_array
current_hops_array = 0
for recipe in recipes:

    for i in range(len(recipe)):

        if recipe[i:i+7] == '"hops":':
            start_hops = i
            end_hops = i + 7

        if recipe[i:i+15] == '"hops Summary":':
            start_summary = i
            end_summary = i + 15             

    recipe_id = current_hops_array
    hops = recipe[end_hops + 2 : start_summary - 2]

    record = str(recipe_id) + ';' + str(hops)
    hops_array.append(record)

    current_hops_array += 1

    print('Creating hops array: ' + str(round((current_hops_array)/len(recipes)* 100,2)) + '%')

#print('/n')
#print(hops_array)

#hops_table
hops_table = []
for h in hops_array:
    recipe_id = h[:str(h).find(';')]
    start_par = []
    end_par = []

    for i in range(len(h)):
        if h[i] == '[':
            start_par.append(i)
        if h[i] == ']':
            end_par.append(i)

    for x in range(len(start_par)):
        #changing the , char to '' in the name
        hops = str(h[start_par[x]+1:end_par[x]])
        char_array = []
        for ff in range(len(hops)):
            if hops[ff] == '"':
                char_array.append(ff)
        try:
            hops = hops[:char_array[0] - 1] + hops[char_array[0]:char_array[1]].replace(',','') + hops[char_array[1] + 1:]
        except:
            hops = hops

        record = str(recipe_id) + ';' + str(hops).replace(',',';').replace('"','').replace(' min;',';').replace(' days;',';').replace('.',',')
        hops_table.append(record)

    print('Creating hops table: ' + str(round((int(h[0])+1)/len(hops_array)* 100,2)) + '%')

#print('/n')
#print(hops_table)




##################Others table
#others_array
current_others_array = 0
for recipe in recipes:

    for i in range(len(recipe)):

        if recipe[i:i+8] == '"other":':
            start_others = i
            end_others = i + 8

        if recipe[i:i+8] == '"yeast":':
            start_yeast = i
            end_yeast = i + 8          

    recipe_id = current_others_array
    others = recipe[end_others + 2 : start_yeast - 2]

    record = str(recipe_id) + ';' + str(others)
    others_array.append(record)

    current_others_array += 1

    print('Creating others array: ' + str(round((current_others_array)/len(recipes)* 100,2)) + '%')
print('/n')
print(others_array)

#others table
others_table = []
for o in others_array:
    recipe_id = o[:str(o).find(';')]
    start_par = []
    end_par = []

    for i in range(len(o)):
        if o[i] == '[':
            start_par.append(i)
        if o[i] == ']':
            end_par.append(i)

    for x in range(len(start_par)):
        #changing the , char to '' in the name
        others = str(o[start_par[x]+1:end_par[x]])

        record = str(recipe_id) + ';' + str(others).replace(',',';').replace('"','').replace(' min.','').replace(' hr.','').replace('.',',')
        others_table.append(record)

    print('Creating others table: ' + str(round((int(o[0])+1)/len(others_array)* 100,2)) + '%')

#print('/n')
#print(others_table)




#################Yeast table
#yeasts_array
current_yeast_array = 0
for recipe in recipes:

    for i in range(len(recipe)):

        if recipe[i:i+8] == '"yeast":':
            start_yeast = i
            end_yeast = i + 8 

        if recipe[i:i+8] == '"views":':
            start_views = i
            end_views = i + 8        

    recipe_id = current_yeast_array
    yeast = recipe[end_yeast + 2 : start_views - 2]

    record = str(recipe_id) + ';' + str(yeast)
    yeast_array.append(record)

    current_yeast_array += 1

    print('Creating yeast array: ' + str(round((current_yeast_array)/len(recipes)* 100,2)) + '%')


#yeasts table
yeast_table = []
cur_y = 0
for y in yeast_array:
    record = str(y.replace(',',';').replace('"','').replace(']','').replace('%','').replace('.',','))
    yeast_table.append(record)

    cur_y += 1

    print('Creating yeast table: ' + str(round((cur_y)/len(others_array)* 100,2)) + '%')

#print('/n')
#print(yeast_table)





#######################Write to Excel
# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('/Users/roland/Documents/Uni/beer_db.xlsx')
worksheet = workbook.add_worksheet('main')
worksheet2 = workbook.add_worksheet('fermentables')
worksheet3 = workbook.add_worksheet('hops')
worksheet4 = workbook.add_worksheet('others')
worksheet5 = workbook.add_worksheet('yeast')

# Some data we want to write to the worksheet.
main_header = ('Recipes_id;Url;Name;Method;Type;Batch;FG;OG;ABV;IBU;Color;PH;View')
fermentables_header = ('Recipes_id;Malt_amount;Malt_name;PPG;L;Malt_bill')
hops_header = ('Recipes_id;Hop_amount;Hop_name;Hop_type;AA;Hop_use;Hop_time;IBU;Hop_bill')
others_header = ('Recipes_id;Other_amount;Other_name;Other_type;Other_use;Other_time')
yeast_header = ('Recipes_id;Yeast_name;Attenuation;Flocculation;Min_temp;Max_temp;Starter')

# Iterate over the data and write it out row by row.

# main
row = 1
col = 0
worksheet.write(0, 0, main_header)
for m in (recipes_array):
    worksheet.write(row, col, m)
    print('Write main table to Excel: ' + str(round((row)/len(recipes_array)* 100,2)) + '%')
    row += 1
    


# fermentables
row = 1
col = 0
worksheet2.write(0, 0, fermentables_header)
for fer in (fermentables_table):
    worksheet2.write(row, col, fer)
    print('Write fermentables table to Excel: ' + str(round((row)/len(fermentables_table)* 100,2)) + '%')
    row += 1


# hops
row = 1
col = 0
worksheet3.write(0, 0, hops_header)
for hop in (hops_table):
    worksheet3.write(row, col, hop)
    print('Write hops table to Excel: ' + str(round((row)/len(hops_table)* 100,2)) + '%')
    row += 1


# others
row = 1
col = 0
worksheet4.write(0, 0, others_header)
for oth in (others_table):
    worksheet4.write(row, col, oth)
    print('Write others table to Excel: ' + str(round((row)/len(others_table)* 100,2)) + '%')
    row += 1


# yeast
row = 1
col = 0
worksheet5.write(0, 0, yeast_header)
for yea in (yeast_table):
    worksheet5.write(row, col, yea)
    print('Write yeast table to Excel: ' + str(round((row)/len(yeast_table)* 100,2)) + '%')
    row += 1

workbook.close()