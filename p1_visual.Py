#%%
import sys
!{sys.executable} -m pip install jupyter pandas altair altair_saver numpy plotnine scikit-learn

import sys
!{sys.executable} -m pip install
altair_saver

import sys
!{sys.executable} -m pip install pandas
import sys
!{sys.executable} -m pip install numpy pandas scikit-learn plotnine altair

#%%
import sys
!{sys.executable} -m pip install --upgrade pip

#%%
import sys
!{sys.executable} -m pip install --upgrade pip

import sys
!{sys.executable}- m pip install radian

import pandas as pd
import numpy as np
import altair as alt
from plotnine import *

import pyarrow.feather as feather
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
#%%
import pandas as pd

gap = pd.read_csv (r'/Users/Zack/Downloads/gapminder.csv').assign(
    pop100k = lambda x : x['pop'] / 100000
)
print(gap)

#practice
#%%
p1_chart = (alt.Chart(gap)
  .encode(
    alt.X('lifeExp', title = "Life Expectancy", scale = alt.Scale(zero=False) ),
    alt.Y('gdpPercap', title = "GDP per capita", scale = alt.Y(type='sqrt')),
    alt.Color('continent'),
    size = 'pop(100k)'
    )
  .mark_circle()
  .facet(
      facet = "year",
      columns = 12
  )
)

#%%
###########   In class   ##############
in_class = alt.Chart(gap)
    .encode(
        x = alt.X('lifeExp',
        scale=alt.Scale(zero=False),
        title = "Life Expectancy"),
        y = alt.Y('gdpPercap', title = "GDP per capita"),
        color = alt.Color('continent', title = 'Continent'),
        size = alt.Size("pop100k", title = 'Population (100k)'))
    .mark_circle()
    .properties(width = 125)
    .facet(column = 'year')


#%%
practice_chart = (alt.Chart(gap)
  .encode(
    alt.X('lifeExp', title = "Life Expectancy", scale = alt.X(type='linear')),
    alt.Y('gdpPercap', title = "GDP per capita", scale = alt.Y(type='sqrt')),
    alt.Color('continent'),
    size = "pop")
  .mark_circle()
  .facet(
      facet = "year",
      columns = 12
  )
)

#%%
df.groupby(['year', 'continent'])['var1].agg(['mean', 'sum', 'count'])

# first perform the aggregation

group_agg = df.groupby(["year", "continent"]).agg({
"var1" : ["mean"],
})


# second rename the columns by joining the column name with the agg function (e.g. "var1_mean")
group_agg.columns = ["gdpPercap".join(x) for x in group_agg.columns.ravel()]

#%%
# You can also pass multiple functions to aggregate the same column e.g:
group_agg = df.groupby(["group1", "group2"]).agg({"var1" : ["mean", "std", "sum"]})





#%%
  #Beginning 2nd Chart
  (gap
  .groupby(['year','continent'])
  .agg({'gdpPercap':
  })
  )


# %%
# Python Questions:
#   fixing scales
#       scale_y_continuous(trans = "sqrt") +
#   theme_bw() 
#   weighted mean for second chart
