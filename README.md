## NUMPY
# NumPy Quick Notes (Practice‑Oriented)

> **Goal:** Yaad rakhne layak short notes + practice solve karne ke cues

---

## 1. NumPy kya hai?

* Fast numerical computation library
* Lists se **faster** aur **vectorized** operations
* ML, Data Analysis, Pandas ke base me hota hai

```python
import numpy as np
```

---

## 2. Array banana (MOST IMPORTANT)

### 2.1 Basic array

```python
np.array([1,2,3])
np.array([[1,2],[3,4]])
```

### 2.2 Zeros / Ones / Same value

```python
np.zeros(5)
np.ones(5)
np.full(5, 7)
```

---

## 3. Range wale arrays

### 3.1 arange

```python
np.arange(10)        # 0–9
np.arange(1, 11)     # 1–10
np.arange(10, 51, 2) # even numbers
```

### 3.2 linspace

```python
np.linspace(0, 1, 5) # equally spaced values
```

---

## 4. Shape, Dimension, Size

```python
arr.shape   # (rows, cols)
arr.ndim    # dimensions
arr.size    # total elements
```

---

## 5. Reshape (INTERVIEW FAVORITE)

```python
np.arange(9).reshape(3,3)
```

Rule:

> total elements must match

---

## 6. Identity Matrix

```python
np.eye(3)
np.identity(3)
```

---

## 7. Random Numbers (CONFUSION AREA)

```python
np.random.rand()        # single float (0–1)
np.random.rand(3,3)     # matrix (0–1)
np.random.randn(5)      # normal distribution (mean=0)
np.random.randint(1,10,5)
```

---

## 8. Basic Math Operations

```python
np.mean(arr)
np.sum(arr)
np.max(arr)
np.min(arr)
np.std(arr)
```

---

## 9. Indexing & Slicing

```python
arr[0]       # first row
arr[:, 1]    # second column
arr[1, 1]    # element
```

---

## 10. Common Mistakes (EXAM ALERT)

❌ `np.arr()`
✅ `np.array()`

❌ `np.random.randint(0,1)` (sirf 0 deta hai)

❌ reshape mismatch

---

## 11. Practice Cue (YAAD RAKHNE KA TARIKA)

Agar question bole:

* **array banao** → `array / zeros / ones`
* **range** → `arange`
* **matrix** → `reshape`
* **identity** → `eye`
* **random** → `rand / randn`

---

## 12. Daily Practice Rule

* 5 NumPy questions
* Code khud likho
* Error aaye → note banao

> **Concept > Ratna**

---

### 📌 GitHub Tip

Is file ko save karo as:

```
NumPy_Quick_Notes.md
```

