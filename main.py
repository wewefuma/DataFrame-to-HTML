import pandas as pd

# creates a dataframe with data from 'dealers.csv'
df = pd.read_csv('dealers.csv', encoding='latin-1')

# sort the values in the 'Branches' column alphabetically
df = df.sort_values(by="Branches", ascending=True)

# fills NaN values with an empty string for cleaner output in HTML
df= df.fillna('')

# can modify as needed
# html template to be written
html_template = """
<div class="card" data-category="{REGION}" href="#mapFrame">
    <button class="actual-card" value="{Google}"  onclick="updateMap(this.value)">
    <h3 class="store-name">{Branches}</h3>
    <p class="store-address">{Address}</p>
    <p class="store-contact">{Contact}</p>
    <p class="store-number">{Mobile}</p>
    </button>
</div>
"""

# init placeholder array value for the generated template
generated_html = []

# for loop reiterating through the dataframe
for index, row in df.iterrows():

    # can modify as needed
    # formats the dictionary values in html_template using the corresponding values in the dataframe
    html_code = html_template.format(
        REGION=row['Region Code'],
        Google=row['Google Map Embed Link'],
        Branches=row['Branches'],
        Address=row['Branch Address'],
        Contact=row['Contact Person'],
        Mobile=row['Mobile number']
    )
    
    # appends the generated code from above to our generated_html array
    generated_html.append(html_code)
    
# opens our output file and writes the values inside the generated_html array
with open("output.html", "w") as f:
    f.write("\n".join(generated_html))
    
print("HTML code generated successfully!")
