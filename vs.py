import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")
matplotlib.rcParams["font.size"]=14
matplotlib.rcParams["figure.figsize"]=(9,5)
matplotlib.rcParams["figure.facecolor"] = "#00000000"

data = sns.load_dataset("iris")
print(data.sample(5))

#scatterplot
sns.scatterplot(x = data.sepal_length, # X-axis
                y = data.sepal_width,  # Y-axis
                hue=data.species,  # Dot color
                s=100);

plt.title("Flowers");
#histogram
plt.title("Distribution of Sepal Width")
sns.displot(data.sepal_width);

plt.title("Flowers")
sns.kdeplot(data.sepal_length, data.sepal_width,
            shade=True, shade_lowest=False)

setosa = data[data.species == "setosa"]
virginica = data[data.species == "virginica"]
versicolor = data[data.species == "versicolor"]

plt.title("Flowers (Setosa & Virginica)")

sns.kdeplot(setosa.sepal_length, setosa.sepal_width, shade=True, cmap='Reds', shade_lowest=False)
sns.kdeplot(virginica.sepal_length, virginica.sepal_width, shade=True, cmap='Blues', shade_lowest=False);
    

plt.show()