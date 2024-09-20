def nb_sommes(n):
    """
    Calcule le nombre de façons de partitionner un entier `n` en sommes d'entiers positifs.

    Cette fonction utilise une fonction auxiliaire récursive `partition_count` pour compter le nombre de partitions
    de `n` en utilisant des entiers jusqu'à `n`.

    Args:
        n (int): L'entier à partitionner.

    Returns:
        int: Le nombre de façons de partitionner l'entier `n`.

    Exemple:
        >>> nb_sommes(4)
        5
    """
    def partition_count(n, max_val):
        if n == 0:
            return 1
        if n < 0 or max_val == 0:
            return 0
        return partition_count(n - max_val, max_val) + partition_count(n, max_val - 1)

    return partition_count(n, n)

def fib(n:int)->int:
    """
    Calcule le nième nombre de Fibonacci en utilisant une fonction auxiliaire récursive.
    Cette fonction utilise une fonction auxiliaire `fib_2` pour calculer le nième nombre de Fibonacci
    de manière efficace en tirant parti des propriétés des indices pairs et impairs dans la séquence de Fibonacci.
    
    Args:
        n (int): La position dans la séquence de Fibonacci à calculer. Doit être un entier non négatif.
    
    Returns:
        int: Le nième nombre de Fibonacci.
    
    Exemple:
        >>> fib(0)
        0
        >>> fib(1)
        1
        >>> fib(10)
        55
    """
    def fib_2(n:int)->int:
        if n == 0:
            return (1,0)
        elif n == 1:
            return (0,1)
        elif n%2 == 0 :
            fn,fn2 = fib_2(n//2)
            return (fn*fn+fn2*fn2,2*fn*fn2+fn2*fn2)
        else:
            fn,fn2 = fib_2(n-1)
            return (fn2,fn+fn2)
    
    return fib_2(n)[1]

def supprime_premier(chaine, cible, result = ""):
    """
    Supprime la première occurrence d'un caractère cible dans une chaîne.

    Args:
        chaine (str): La chaîne de caractères dans laquelle chercher.
        cible (str): Le caractère à supprimer.
        result (str, optional): La chaîne résultante après suppression. Par défaut, c'est une chaîne vide.

    Returns:
        tuple: Un tuple contenant un booléen indiquant si le caractère cible a été trouvé et supprimé,
               et la chaîne résultante après suppression de la première occurrence du caractère cible.
    """
    if len(chaine) == 0:
        return (False,result)
    elif chaine[0] == cible:
        return (True,result + chaine[1:])
    return supprime_premier(chaine[1:], cible, result + chaine[0])

def anagrammes(chaine1, chaine2):
    """
    Détermine si deux chaînes de caractères sont des anagrammes l'une de l'autre.

    Un anagramme est un mot ou une phrase formé en réarrangeant les lettres d'un autre mot ou d'une autre phrase,
    en utilisant typiquement toutes les lettres originales exactement une fois.

    Args:
        chaine1 (str): La première chaîne à comparer.
        chaine2 (str): La deuxième chaîne à comparer.

    Returns:
        bool: True si les chaînes sont des anagrammes, False sinon.
    """
    if len(chaine1) != len(chaine2):
        return False
    if len(chaine1) == 0:
        return True
    if chaine1[0] in chaine2:
        return anagrammes(chaine1[1:], supprime_premier(chaine2, chaine1[0])[1])
    return False


