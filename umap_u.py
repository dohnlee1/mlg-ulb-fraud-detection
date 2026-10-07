from umap import UMAP

class UnsupervisedUMAP(UMAP):
    def fit(self, X, y=None, *args, **kwargs):
        return super().fit(X, None, *args, **kwargs)

    def fit_transform(self, X, y=None, *args, **kwargs):
        return super().fit_transform(X, None, *args, **kwargs)
