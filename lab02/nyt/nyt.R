load("pca-examples.Rdata")

nyt.pca <- prcomp(nyt.frame[, -1])
nyt.latent.sem <- nyt.pca$rotation

writeLines("30 elements with highest values for first component :")
signif(sort(nyt.latent.sem[, 1], decreasing = TRUE)[1:30], 2)
writeLines("")

writeLines("30 elements with lowest values for first component :")
signif(sort(nyt.latent.sem[, 1], decreasing = FALSE)[1:30], 2)
writeLines("")

writeLines("30 elements with highest values for second component :")
signif(sort(nyt.latent.sem[, 2], decreasing = TRUE)[1:30], 2)
writeLines("")

writeLines("30 elements with lowest values for second component :")
signif(sort(nyt.latent.sem[, 2], decreasing = FALSE)[1:30], 2)
writeLines("")

plot(nyt.pca$x[, 1:2], type="n")

points(nyt.pca$x[nyt.frame[, "class.labels"] == "art", 1:2], pch="a", col="green")

points(nyt.pca$x[nyt.frame[, "class.labels"] == "music", 1:2], pch="m", col="brown")
