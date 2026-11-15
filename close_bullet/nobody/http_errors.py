import requests


def _error_blob(exc: BaseException) -> str:
    parts = [f"{type(exc).__name__}: {exc}"]
    chain = exc
    while chain.__cause__ is not None:
        chain = chain.__cause__
        parts.append(str(chain))
    return " ".join(parts)


def friendly_http_error(exc: BaseException) -> Exception:
    text = _error_blob(exc)
    low = text.lower()
    if "407" in text or "proxy authentication" in low:
        return Exception(
            "[Proxy] Authentication failed (407). Check credentials in proxy.txt "
            "or disable proxy in config.ini: [Proxy] active = 0"
        )
    if "unable to connect to proxy" in low or "proxyerror" in low:
        return Exception(
            "[Proxy] Unable to connect to proxy. Check proxy.txt or set active = 0"
        )
    if "tunnel connection failed" in low:
        return Exception(
            "[Proxy] Tunnel connection failed (proxy down or bad URL). Try active = 0"
        )
    if "certificateerror" in low or "ssl" in type(exc).__name__.lower():
        return Exception(
            "[SSL] Certificate verification failed via proxy/network. Try another proxy or active = 0"
        )
    if "max retries exceeded" in low and "proxy" in low:
        return Exception(
            "[Proxy] Max retries exceeded — proxy is down or requires authentication."
        )
    return exc if isinstance(exc, Exception) else Exception(text)


def wrap_session_request(session):
    if getattr(session, "_cb_http_errors_wrapped", False):
        return session

    original = session.request

    def request(method, url, **kwargs):
        try:
            return original(method, url, **kwargs)
        except requests.RequestException as e:
            raise friendly_http_error(e) from e

    session.request = request  # type: ignore[method-assign]
    session._cb_http_errors_wrapped = True
    return session