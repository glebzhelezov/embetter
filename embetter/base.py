from sklearn.base import BaseEstimator, TransformerMixin


class EmbetterBase(TransformerMixin, BaseEstimator):
    """Base class for feature transformers in this library"""

    def

    def fit(self, X, y=None):
        """No-op."""
        return self

    def partial_fit(self, X, y=None):
        """No-op."""
        return self
