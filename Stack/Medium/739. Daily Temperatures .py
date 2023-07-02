def d_temps(temps):
    ln = len(temps)
    st = []
    result = [0] * ln
    for i in range(ln):
        while st and temps[i] > st[-1]:
            result[i - 1] = st.pop()
        st.append(i)

    print(st)
    print(result)


temperatures = [75, 76, 73]

print(d_temps(temperatures))